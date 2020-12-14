from flask import current_app, g, session, jsonify
from functools import wraps


def login_required(view_func):
    @wraps(view_func)
    def wrapper(*agrs, **kwargs):
        user_id = session.get("user_id")
        if not user_id:
            return jsonify(errno="-1", errmsg="用户未登录")
        else:
            g.user_id = user_id
            return view_func(*agrs, **kwargs)
    return wrapper
