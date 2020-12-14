from . import api
from ihome.utilis.captcha.captcha import captcha   # 生成验证码图片
from ihome.utilis.response_code import RET
from ihome import redis_store, constants
from ihome.models import User
from ihome.libs.yuntongxun.sms import CCP
from flask import current_app, make_response, jsonify, request
from ihome.tasks.task_sms import send_sms
import random


# 路由规则的编写可以遵守restful协议，既不要在路由中使用动词
# 比如: /get_goods  /add_goods等
# HTTP的请求方式正好可以对应增删改查  post/delete/put/get
# 参数可以在url中给出  /goods/ID
# 127.0.0.1:5000/api/v1.0/image_codes/<image_code_id>
@api.route("/image_codes/<image_code_id>")
def get_image_code(image_code_id):
    """
    获取验证码图片，并返回给前端
    register.html页面一加载，就通过js脚本，补充上src字段，即本函数接口  <img src="/api/v1.0/123456789>
    浏览器解析页面时，就根据src发送请求
    """
    
    # 一般视图函数的作用
    # 获取数据  已经通过转换器获取
    # 验证数据  没有传递image_code_id不会进入到这个视图函数
    # 业务逻辑处理
    # 生成验证码图片
    # 图片的名字  真实的验证码文本  图片数据
    name, text, image_data = captcha.generate_captcha()

    # 将图片id和验证码文本存到redis中，并且设置有效期
    # hash: "image_codes": {"id1":"abc", "id2":"def"}  哈希可以保存，但是只能对一整个数据设置有效期
    # 所以改用string： "image_codes_id1": "abc", "image_codes_id2": "def"
    # 一般把常量也单独放到一个文件中去
    try:
        redis_store.setex("image_codes_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        # 记录日志
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="save image codes failed.")

    # 返回图片
    response = make_response(image_data)
    response.headers["Content-Type"] = "image/jpg"
    return response


# /api/v1.0/sms_codes/<mobile>?image_codes_id=xxx&image_code=xxxx
@api.route("/sms_codes/<re(r'1[35789]\d{9}'):mobile>")
def get_sms_code(mobile):
    """获取短信验证码"""
    # 获取数据
    image_codes_id = request.args.get("image_codes_id")
    image_code = request.args.get("image_code")

    # 验证数据
    if not all([image_codes_id, image_code]):
        return jsonify(errno=RET.PARAMERR, errmsg="数据不完整")

    # 业务逻辑处理
    # 1. 验证图片验证码正确性
    # 从redis中读取真实的图片验证码
    try:
        real_image_code = redis_store.get("image_codes_%s" % image_codes_id)  # 此时读取出来的值是二进制格式的！
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="redis数据库异常")
    
    # 判断图片验证码是否过期
    if real_image_code is None:
        # 图片验证码不存在或者过期
        return jsonify(errno=RET.NODATA, errmsg="图片验证码过期")
    
    # 删除redis中的图片验证码，防止用户使用同一个验证码验证多次
    try:
        redis_store.delete("image_codes_%s" % image_codes_id)
    except Exception as e:
        current_app.logger.error(e)
    
    # 与用户输入的进行对比
    if real_image_code.decode('utf-8').lower() != image_code.lower():  # 在比较时，必须转为字符串才能比较，否则一直报图片验证码填写错误
        # 用户填写的图片验证码错误
        return jsonify(errno=RET.DATAERR, errmsg="图片验证码填写错误")
        

    # 2. 发送短信验证码逻辑
    # 判断此手机号是否在60s内已经发送过短信验证码，如果是，则直接返回
    try:
        send_flag = redis_store.get("send_sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if send_flag is not None:
            # 表示发送过
            return jsonify(errno=RET.REQERR, errmsg="请求过于频繁，请60秒后重试")

    # 判断手机号是否已经存在
    # try:
    #     user = User.query.filter_by(mobile=mobile).first()
    # except Exception as e:
    #     current_app.logger.error(e)
    # else:   # 如果发生异常 user变量不存在
    #     if user is not None:
    #         # 用户已经存在
    #         return jsonify(errno=RET.DATAEXIST, errmsg="手机号已经存在")
    
    # 如果不存在，就可以生成短信验证码
    sms_code = "%06d" % random.randint(0, 999999)  # %06d 表示六位数，不满六位用0补充

    # 保存真实的短信验证码到redis数据库
    try:
        redis_store.setex("sms_codes_%s" % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # 保存给这个手机号发送过短信的记录，防止用户在60s内多次点击获取短信验证码
        redis_store.setex("send_sms_code_%s" % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="redis数据库异常")

    # 发送短信
    try:
        ccp = CCP()
        result = ccp.send_template_sms(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES/60)], 1)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="发送短信异常")

    # 改用celery异步执行发送短信的任务
    # 调用后立即返回,返回值是一个对象
    # result_obj = send_sms.delay(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES/60)], 1)
    # print("result_obj = " % result_obj)
    # 暂时发不出短信，报网络错误
    send_sms.delay(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES/60)], 1)

    # 通过异步任务对象，获取任务结果
    # get方法默认是阻塞的
    # ret = result_obj.get()
    # print("ret = %s" % ret)

    # 返回
    # if result == 0:
    #     return jsonify(errno=RET.OK, errmsg="发送成功")
    # else:
    #     return jsonify(errno=RET.THIRDERR, errmsg="发送失败")
    return jsonify(errno=RET.OK, errmsg="发送成功")
