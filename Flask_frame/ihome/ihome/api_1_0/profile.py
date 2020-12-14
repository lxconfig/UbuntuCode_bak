
from . import api
from ihome.utilis.commons import login_required
from flask import g, jsonify, current_app, request, session
from ihome.utilis.response_code import RET
from ihome.models import User
from ihome.utilis.image_storage import storage
from ihome import db, constants
import re


@api.route("/users/avatar", methods=["POST"])
@login_required
def set_user_avatar():
    """设置用户头像"""
    # 获取参数  图片  用户id(已经保存在g对象中)
    image_file = request.files.get("avatar")
    user_id = g.user_id

    # 校验参数
    if image_file is None:
        return jsonify(errno=RET.PARAMERR, errmsg="未上传图片")
    
    image_data = image_file.read()

    # 业务逻辑处理
    # 1. 调用七牛的接口，将图片数据上传到七牛
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="上传图片失败")
    
    # 2. 保存文件名到数据库
    try:
        User.query.filter_by(id=user_id).update({"avatar_url": file_name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存图片信息失败")

    # 返回
    avatar_url = constants.QINIU_URL_DOMAIN + file_name
    return jsonify(errno=RET.OK, errmsg="上传图片成功", data={"avatar_url": avatar_url})



@api.route("/users/name", methods=["POST"])
@login_required
def set_user_name():
    """设置用户名"""
    # 获取参数  用户名  用户id
    request_data = request.get_json()
    user_name = request_data.get("name")
    user_id = g.user_id

    # 校验参数
    if not user_name:
        return jsonify(errno=RET.PARAMERR, errmsg="未填写用户名")

    # 业务逻辑处理
    # 1. 判断用户名是否已经存在
    try:
        user = User.query.filter_by(name=user_name).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")
    else:
        if user:
            # 用户名存在
            return jsonify(errno=RET.DATAEXIST, errmsg="用户名已存在")
    
    # 2. 保存用户名
    try:
        User.query.filter_by(id=user_id).update({"name": user_name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    # 修改session中的name字段
    session["name"] = user_name
    # 返回
    return jsonify(errno=RET.OK, errmsg="设置成功", data={"user_name": user_name})



@api.route("/users/info", methods=["GET"])
@login_required
def get_user_info():
    """获取用户资料，填充到个人主页my.html"""

    # 获取参数  user_id
    user_id = g.user_id

    # 校验参数  在login_required装饰器中已经校验过

    # 业务逻辑处理
    # 根据user_id到数据库中取数据
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    # 返回
    if not user.avatar_url:
        # 设置默认头像
        avatar_url = constants.QINIU_URL_DOMAIN + "1.jpg"
    else:
        avatar_url = constants.QINIU_URL_DOMAIN + user.avatar_url
    return jsonify(errno=RET.OK, errmsg="查询成功", data={"user_name": user.name, "mobile": user.mobile, "avatar_url": avatar_url})



@api.route("/users/auth", methods=["POST", "GET"])
@login_required
def user_auth():
    """用户实名认证(设置姓名及身份证号)"""
    # 获取参数  用户id  真实姓名  身份证号
    user_id = g.user_id

    if request.method == "POST":
        request_data = request.get_json()
        real_name = request_data.get("real_name")
        id_card = request_data.get("id_card")

        # 校验参数
        if not all([real_name, id_card]):
            return jsonify(errno=RET.PARAMERR, errmsg="数据填写不完整")
        
        if not re.match(r"^\d{17}[0-9xX]$", id_card):
            return jsonify(errno=RET.PARAMERR, errmsg="身份证号格式错误")

        # 业务逻辑处理
        # 1. 将真实姓名和身份证号存入数据库,并且只有用户的real_name和id_card为空时，才保存数据
        try:
            user = User.query.filter_by(id=user_id, real_name=None, id_card=None).update({"real_name": real_name, "id_card": id_card})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="数据库异常")

        # 返回
        return jsonify(errno=RET.OK, errmsg="实名认证成功")
    else:
        # get方式时，只需要去数据库查询数据
        try:
            user = User.query.filter_by(id=user_id).first()
        except Exception as e:
            current_app.logger.error(e)
        else:
            if not user.real_name and not user.id_card:
                # 没有实名认证数据
                return jsonify(errno=RET.NODATA, errmsg="用户没有实名认证")
            else:
                return jsonify(errno=RET.OK, errmsg="查询成功", data={"real_name": user.real_name, "id_card": user.id_card})
