from flask import Flask, render_template, request, jsonify, make_response, session, g
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from datetime import datetime
from libs.captcha.captcha import captcha
from libs.yuntongxun.sms import CCP
from werkzeug.routing import BaseConverter
from login_required import login_required
import pymysql, redis, re, random


pymysql.install_as_MySQLdb()


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:lixuan@127.0.0.1:3306/todolist"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "HDGSDIOskcgnisodn593y2598dg"


app = Flask(__name__)
Bootstrap(app)

app.config.from_object(Config)
db = SQLAlchemy(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

redis_store = redis.StrictRedis(host="127.0.0.1", port="6379", db=2)


class BaseModel:
    """模型类的基类，用于记录创建时间、更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class User(BaseModel, db.Model):
    """用户模型类"""
    __tablename__ = "todolist_users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    mobile = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    avatar_url = db.Column(db.String(128), default="")
    events = db.relationship("Event", backref="user")


class Kind(BaseModel, db.Model):
    """事件种类模型类"""
    __tablename__ = "todolist_kinds"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    events = db.relationship("Event", backref="kind")


class Event(BaseModel, db.Model):
    """待办事项模型类"""
    __tablename__ = "todolist_events"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, nullable=False)
    isCompleted = db.Column(db.Integer, nullable=False, default=0)  # 默认都是0，表示未完成
    user_id = db.Column(db.Integer, db.ForeignKey("todolist_users.id"), nullable=False)
    kind_id = db.Column(db.Integer, db.ForeignKey("todolist_kinds.id"), nullable=False)



class MyConverter(BaseConverter):
    def __init__(self, url_map, regex):
        self.regex = regex
        super().__init__(url_map)

app.url_map.converters["re"] = MyConverter


@app.route("/<re(r'.*'):static_file>")
def get_static_page(static_file):
    """提供静态页面"""
    if not static_file:
        static_file = "index.html"
    return render_template(static_file)


# users/imgCode?imgID=xxxxx
@app.route("/users/imgCode")
def get_image_code():
    """生成图片验证码"""
    image_id = request.args.get("imgID")
    name, image_code, image_data = captcha.generate_captcha()
    # print(name, image_code, iamge_data)
    print(image_id)
    try:
        redis_store.setex("img_code_%s" % image_id, 300, image_code)
    except Exception:
        return jsonify(error="-1", errmsg="数据库异常")
    # response = make_response(image_data)
    # response.headers["Content-Type"] = "image/jpg"
    # return response
    return image_data, 200, {"Content-Type": "image/jpg"}


@app.route("/users/smsCode", methods=["POST"])
def get_sms_code():
    """获取短信验证码"""
    request_data = request.get_json()
    image_code = request_data.get("imgCode")
    mobile = request_data.get("mobile")
    image_id = request.args.get("imgID")

    print(image_id)

    if not all([mobile, image_code]):
        return jsonify(error="-1", errmsg="参数填写不完整")
    
    if not re.match(r"1[35789]\d{9}", mobile):
        return jsonify(error="-1", errmsg="手机号格式错误")

    try:
        flag = redis_store.get("sended_sms_code_%s" % mobile)
    except Exception:
        pass
    else:
        if flag:
            return jsonify(error="-1", errmsg="请求过于频繁,请稍后再试!")

    # 判断手机号是否存在
    
    try:
        real_image_code = redis_store.get("img_code_%s" % image_id)
    except Exception:
        return jsonify(error="-1", errmsg="数据库异常")
    print(real_image_code.decode("utf-8"), image_code)
    if real_image_code.decode("utf-8").lower() != image_code.lower():
        return jsonify(error="-1", errmsg="图片验证码填写错误")
    
    # 发送短信
    sms_code = "%06d" % random.randint(0, 999999)
    try:
        redis_store.setex("sms_code_%s" % mobile, 3600, sms_code)
        redis_store.setex("sended_sms_code_%s" % mobile, 300, 1)
    except Exception:
        pass

    ccp = CCP()
    try:
        ret = ccp.send_template_sms(mobile, datas=[sms_code, 5], temp_id=1)
    except Exception:
        return jsonify(error="-1", errmsg="发送短信错误")

    if ret == 0:
        return jsonify(errno="0", errmsg="发送成功")
    else:
        return jsonify(errno="-1", errmsg="发送失败")


@app.route("/users/register", methods=["POST"])
def register():
    """注册页"""
    # 获取数据
    request_data = request.get_json()
    username = request_data.get("username")
    mobile = request_data.get("mobile")
    email = request_data.get("email")
    sms_code = request_data.get("sms_code")
    pwd = request_data.get("pwd")
    pwd2 = request_data.get("pwd2")
    print(username, mobile, email, sms_code, pwd, pwd2)

    if not all([username, mobile, email, sms_code, pwd, pwd2]):
        return jsonify(errno="-1", errmsg="参数不完整")
    
    if not re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
        return jsonify(errno="-1", errmsg="邮箱格式不正确")
    
    try:
        real_sms_code = redis_store.get("sms_code_%s" % mobile)
    except Exception:
        return jsonify(errno="-1", errmsg="数据库错误")
    
    if real_sms_code.decode("utf-8") != sms_code:
        return jsonify(errno="-1", errmsg="短信验证码填写错误")
    
    if pwd != pwd2:
        return jsonify(errno="-1", errmsg="两次密码不一致")
    
    try:
        user = User(name=username, mobile=mobile, email=email, password=pwd, avatar_url="1.jpg")
        db.session.add(user)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify(errno="-1", errmsg="数据库错误")
    
    session["user_id"] = user.id
    session["username"] = username    

    return jsonify(errno="0", errmsg="注册成功")


@app.route("/sessions")
def hasLogin():
    """判断用户是否已经登录"""
    username = session.get("username")
    if username:
        return jsonify(errno="0", errmsg="用户已登录", data={"username": username})
    return jsonify(errno="-1", errmsg="用户未登录")


@app.route("/users/login", methods=["POST"])
def login():
    """用户登录"""
    request_data = request.get_json()
    mobile = request_data.get("mobile")
    password = request_data.get("password")

    if not re.match(r"1[356789]\d{9}", mobile):
        return jsonify(errno="-1", errmsg="手机号格式错误")
    
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception:
        return jsonify(errno="-1", errmsg="数据库异常")
    else:
        if not user:
            return jsonify(errno="-1", errmsg="手机号不存在")
    
    if user.password != password:
        return jsonify(errno="-1", errmsg="手机号或密码错误")
    
    session["user_id"] = user.id
    session["username"] = user.name

    return jsonify(errno="0", errmsg="登录成功")


@app.route("/events")
def get_user_events():
    """获取用户的待办事项"""
    user_id = session.get("user_id")
    if not user_id:
        return render_template("events.html")
    try:
        user = User.query.filter_by(id=user_id).first()
    except Exception:
        return jsonify(errno="-1", errmsg="数据库异常")
    
    events = {
        "events": user.events
    }
    return render_template("events.html", **events)


@app.route("/kinds", methods=["POST"])
@login_required
def add_new_kinds():
    request_data = request.get_json()
    kind_name = request_data.get("kind_name")

    if not kind_name:
        return jsonify(errno="-1", errmsg="请填写类别名")
    
    try:
        kind = Kind.query.filter_by(name=kind_name).first()
    except Exception:
        return jsonify(errno="-1", errmsg="数据库异常")

    if kind:
        return jsonify(errno="-1", errmsg="该类别已经存在")

    try:
        kind = Kind(name=kind_name)
        db.session.add(kind)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify(errno="-1", errmsg="数据库异常")
    return jsonify(errno="0", errmsg="添加成功")   


@app.route("/addEvents", methods=["POST"])
@login_required
def add_users_events():
    request_data = request.get_json()
    title = request_data.get("title")
    kind_id = request_data.get("kind_id")
    user_id = g.user_id
    if not all([title, kind_id, user_id]):
        return jsonify(errno="-1", errmsg="数据不完整")
    try:
        event = Event(title=title, user_id=user_id, kind_id=kind_id)
        db.session.add(event)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify(errno="-1", errmsg="数据库异常")
    return jsonify(errno="0", errmsg="添加成功")


@app.route("/success", methods=["POST"])
@login_required
def success_events():
    request_data = request.get_json()
    event_id = request_data.get("event_id")
    user_id = g.user_id
    if not event_id:
        return jsonify(errno="-1", errmsg="请输入编号")
    try:
        event = Event.query.filter_by(user_id=user_id, id=event_id).first()
    except Exception:
        return jsonify(errno="-1", errmsg="数据库异常")
    else:
        if not event:
            return jsonify(errno="-1", errmsg="编号不存在")
    try:
        event.isCompleted = 1
        db.session.add(event)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify(errno="-1", errmsg="数据库异常")
    return jsonify(errno="0", errmsg="待办事件状态更新成功")


if __name__ == "__main__":
    manager.run()