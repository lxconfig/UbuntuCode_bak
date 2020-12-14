from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)
pymysql.install_as_MySQLdb()


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql://root:lixuan@127.0.0.1:3306/flasktest"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

db = SQLAlchemy(app)


# 一类
class User(db.Model):
    """用户类"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    houses = db.relationship("House", backref="user")   # 相当于在House类中增加属性user


# 多类
class House(db.Model):
    """房屋类"""
    __tablename__ = "houses_info"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))   # 在多类中定义外键



if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()

    # user1 = User(name="zhangsan")
    # user2 = User(name="lisi")
    # user3 = User(name="wangwu")
    # user4 = User(name="zhaoliu")
    # db.session.add_all([user1, user2, user3, user4])
    # db.session.commit()

    # house1 = House(name="中粮", user_id=1)
    # house2 = House(name="碧桂园", user_id=2)
    # house3 = House(name="星翰宛", user_id=3)
    # house4 = House(name="高的地产", user_id=2)
    # house5 = House(name="星河湾", user_id=4)
    # # db.session.add_all([house1, house2, house3, house4])
    # db.session.add(house5)
    # db.session.commit()

    # 一查多，查看用户拥有的房屋
    user = User.query.get(2)
    print(user.houses)   # [<House 2>, <House 4>]
    print(user.houses[0].name)   # 碧桂园

    # 多查一，查看房屋的用户是谁
    # 通过在一类设置的backref字段来查
    house = House.query.get(1)
    print(house.user)  # <User 1>
    print(house.user.name)  # zhangsan
    # 或者通过本身的外键user_id来查
    u = User.query.get(house.user_id)
    print(u)  # <User 1>
    print(u.name)  # zhangsan


    house_query = House.query.filter(House.id == 1).order_by(House.id)
    print("house.query:", house_query)   # 还没有做查询，输出的只是sql语句

    page_obj = house_query.paginate(page=1, per_page=2, error_out=False)
    print("page_obj:", page_obj)  # 分页对象 <flask_sqlalchemy.Pagination object at 0x0000026CC2821E48>
    house = page_obj.items   # 此时才拿到真正的查询结果  [<House 1>]
    print("house:", house)

    total_pages = page_obj.pages
    print("total_pages:", total_pages)