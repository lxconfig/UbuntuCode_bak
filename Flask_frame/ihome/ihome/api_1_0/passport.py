
from . import api
from ihome.utilis.response_code import RET
from ihome import redis_store, db, constants
from ihome.models import User
from flask import request, jsonify, current_app, session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
import re


# 参数的格式是json
@api.route("/users", methods=['POST'])
def register():
    """用户注册"""

    # 获取数据
    # 直接将前端的json数据，解析成字典
    request_data = request.get_json()
    mobile = request_data.get("mobile")
    sms_code = request_data.get("sms_code")
    password = request_data.get("password")
    password2 = request_data.get("password2")

    # 校验数据
    if not all([mobile, sms_code, password, password2]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")

    # 校验手机号格式
    if not re.match(r"1[35789]\d{9}", mobile):
        # 手机号格式错误
        return jsonify(errno=RET.PARAMERR, errmsg="手机号格式错误")
    
    # 校验密码一致性
    if password != password2:
        return jsonify(errno=RET.PARAMERR, errmsg="两次密码不一致")
    
    # 业务逻辑处理
    # 1. 从redis中取出真实的短信验证码
    try:
        real_sms_code = redis_store.get("sms_codes_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="redis数据库异常")

    # 2. 判断短信验证码是否过期
    if real_sms_code is None:
        # 表示短信验证码过期或不存在
        return jsonify(errno=RET.DATAEXIST, errmsg="短信验证码过期")

    # 3. 判断短信验证码是否填写正确
    if real_sms_code.decode("utf-8") != sms_code:
        return jsonify(errno=RET.DATAERR, errmsg="短信验证码填写错误")

    # 4. 判断用户手机号是否注册过,可以放到保存用户时去做。因为设计数据库时，mobile字段设置了unique
    # 重复的mobile值一定会报错

    # 5. 保存用户数据到数据库
    user = User(name=mobile, mobile=mobile)
    # 使用werkzeug工具箱中封装的方法来生成加密的password，并且直接再模型类中就计算好
    # 通过property设置成一个属性
    user.password = password
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as I:
        # commit操作出现异常后，要回滚到上一次commit的状态
        db.session.rollback()
        # 表示手机号重复
        current_app.logger.error(I)
        return jsonify(errno=RET.DATAEXIST, errmsg="手机号已存在")
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询数据库异常")

    # 6. 记录用户登录状态到session中
    session["name"] = mobile
    session["mobile"] = mobile
    session["user_id"] = user.id

    # 返回
    return jsonify(errno=RET.OK, errmsg="注册成功")


# 参数的格式是json
@api.route("/login", methods=["POST"])
def login():
    """用户登录"""
    # 获取参数
    request_data = request.get_json()
    mobile = request_data.get("mobile")
    password = request_data.get("password")

    # 校验参数
    if not all([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg="数据填写不完整")

    # 业务逻辑处理
    # 1. 判断手机号格式是否正确
    if not re.match(r"1[35789]\d{9}", mobile):
        return jsonify(errno=RET.DATAERR, errmsg="手机号格式错误")

    # 2. 判断错误次数是否超过限制，是则返回
    user_ip = request.remote_addr   # 请求用户的ip地址
    try:
        access_nums = redis_store.get("access_nums_%s" % user_ip)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if access_nums is not None and int(access_nums) >= constants.LOGIN_ERROR_MAX_TIMES:
            return jsonify(errno=RET.REQERR, errmsg="错误次数过多，请稍后重试")
    
    # 3. 判断手机号是否存在
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="获取用户信息失败")

    # 4. 将手机号的判断和密码匹配放到一起
    if user is None or not check_password_hash(user.password_hash, password):
        # 如果验证失败，则要记录一次错误的尝试
        try:
            redis_store.incr("access_nums_%s" % user_ip)   # incr是为当前键的值加1，若不存在，则初始化为0，然后再加1
            redis_store.expire("access_nums_%s" % user_ip, constants.LOGIN_ERROR_FORBID_TIME)   # 只有在第5次时，这个时间限制才真正有意义
        except Exception as e:
            current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="手机号或密码错误")
    
    # 5. 记录用户登录状态到session中
    session["name"] = user.name
    session["mobile"] = user.mobile
    session["user_id"] = user.id

    # 返回
    return jsonify(errno=RET.OK, errmsg="登录成功")


@api.route("/session", methods=["GET"])
def isLogin():
    """判断用户是否登录"""
    name = session.get("name")
    if name is None:
        return jsonify(errno=RET.SESSIONERR, errmsg="未登录")
    else:
        return jsonify(errno=RET.OK, errmsg="已登录", name=name)


@api.route("/session", methods=["DELETE"])
def logout():
    """用户登出"""
    # 清空session数据
    session.clear()
    return jsonify(errno=RET.OK, errmsg="OK")