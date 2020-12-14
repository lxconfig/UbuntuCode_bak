from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
from ihome.utilis.response_code import RET
import functools


class MyConverter(BaseConverter):
    """自定义转换器"""
    def __init__(self, url_map, regex):
        self.regex = regex
        super().__init__(url_map)


# 定义验证登录状态的装饰器
def login_required(view_func):
    # 一般在装饰器的内层函数中，在套一个带参数的装饰器functools.wraps(func)，参数func就是外层装饰器的参数
    # 意义在于：还原被装饰的函数一些属性，如 __name__, __doc__等
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 判断用户的登录状态
        user_id = session.get("user_id")
        # 如果是登录的，就执行视图函数
        if user_id is not None:
            # 函数之间可以通过g对象来保存数据,被装饰的函数就可以从g对象中取出user_id来使用
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录") 
    return wrapper