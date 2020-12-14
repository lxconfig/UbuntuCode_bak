from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash
from ihome import constants


class BaseModel:
    """模型类的基类，主要为其他表的数据记录创建时间和更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class User(BaseModel, db.Model):
    """用户模型类"""

    __tablename__ = "ih_user_profile"

    id = db.Column(db.Integer, primary_key=True)
    mobile = db.Column(db.String(11), unique=True, nullable=False)
    name = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    real_name = db.Column(db.String(32))  # 用户真实姓名
    id_card = db.Column(db.String(20))    # 用户身份证号码
    avatar_url = db.Column(db.String(128))  # 用户头像的url地址
    houses = db.relationship("House", backref="user")  # 用于查询用户的所有房屋
    orders = db.relationship("Order", backref="user")  # 用于查询用户的订单

    @property
    def password(self):
        # 由于这个属性读取没有意义，所以在试图读取此值的时候直接返回异常
        raise AttributeError("此属性只能设置，不能读取") 
    
    @password.setter
    def password(self, value):
        """生成加密的密码"""
        # 一般密码加密要加上盐值，最后保存的密码应该是这样的形式：abc$sdguisbuibauefna,其中abc表示盐值，$分隔，后面的值代表真正加密后的值
        self.password_hash = generate_password_hash(value)


class Area(BaseModel, db.Model):
    """城区模型类"""

    __tablename__ = "ih_area_info"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    houses = db.relationship("House", backref="area")  # 用于查询某个城区的房屋

    def to_dict(self):
        """将对象转为字典"""
        d = {
            "area_id": self.id,
            "area_name": self.name
        }
        return d


# 房屋设施表，建立房屋与设施的多对多关系
# db.Table可以直接创建表
house_facility = db.Table(
    "ih_house_facility",
    db.Column("house_id", db.Integer, db.ForeignKey("ih_house_info.id"), primary_key=True),  # 房屋id
    db.Column("facility_id", db.Integer, db.ForeignKey("ih_facility_info.id"), primary_key=True)  # 设施id
)


class House(BaseModel, db.Model):
    """房屋信息模型类"""

    __tablename__ = "ih_house_info"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False)  # 房屋主人的用户编号
    area_id = db.Column(db.Integer, db.ForeignKey("ih_area_info.id"), nullable=False)     # 房屋所属城区编号
    title = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Integer, default=0)
    address = db.Column(db.String(512), default="")
    room_count = db.Column(db.Integer, default=1)  # 房间数目
    acreage = db.Column(db.Integer, default=0)   # 房屋面积
    unit = db.Column(db.String(32), default="")  # 房屋单元， 如几室几厅
    capacity = db.Column(db.Integer, default=1)  # 房屋容纳的人数
    beds = db.Column(db.String(64), default="")  # 房屋床铺的配置
    deposit = db.Column(db.Integer, default=0)  # 房屋押金
    min_days = db.Column(db.Integer, default=1)  # 最少入住天数
    max_days = db.Column(db.Integer, default=0)  # 最多入住天数，0表示不限制
    order_count = db.Column(db.Integer, default=0)  # 预订完成的该房屋的订单数
    index_image_url = db.Column(db.String(256), default="")  # 房屋主图片的路径
    # secondary表示要去house_facility表进行二次查询
    facilities = db.relationship("Facility", secondary=house_facility)  # 房屋的设施
    images = db.relationship("HouseImage")  # 房屋的图片
    orders = db.relationship("Order", backref="house")  # 房屋的订单

    def to_dict(self):
        """将房屋的一些基本信息转为字典，方便构造参数传给前端"""
        house_dict = {
            "house_id": self.id,
            "title": self.title,
            "area_name": self.area.name,  # 从Area中设置来的area属性
            "price": self.price,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "image_url": constants.QINIU_URL_DOMAIN + self.index_image_url if self.index_image_url else "",  # 从User类中设置来的user属性
            "user_avatar": constants.QINIU_URL_DOMAIN + self.user.avatar_url if self.user.avatar_url else "",
            "address" : self.address,
            "room_count": self.room_count,
            "order_count": self.order_count
        }
        return house_dict
    
    def full_to_dict(self):
        """将房屋的所有信息转为字典"""
        house_dict = {
            "house_id": self.id,
            "user_id": self.user_id,
            "user_name": self.user.name,
            "title": self.title,
            "price": self.price,
            "user_avatar": constants.QINIU_URL_DOMAIN + self.user.avatar_url if self.user.avatar_url else "",
            "address" : self.address,
            "room_count": self.room_count,
            "acreage": self.acreage,
            "unit": self.unit,
            "capacity": self.capacity,
            "deposit": self.deposit,
            "beds": self.beds,
            "min_days": self.min_days,
            "max_days": self.max_days,
        }

        # 房屋图片
        img_url = []
        for image in self.images:
            img_url.append(constants.QINIU_URL_DOMAIN + image.url)
        
        # 房屋设置
        facilities = []
        for facility in self.facilities:
            facilities.append(facility.id)
        
        # 评论信息
        comments = []
        orders = Order.query.filter(Order.house_id==self.id, Order.status == "COMPLETE", Order.comment != None).order_by(Order.update_time.desc()) \
            .limit(constants.HOUSE_DETAIL_COMMENT_DISPLAY_COUNTS)
        for order in orders:
            comment = {
                "comment": order.comment,   # 评论内容
                "user_name": order.user.name if order.user.name != order.user.mobile else "匿名用户",  # 如果有设置名字，就显示名字，否则就显示匿名用户，不要显示成手机号
                "create_time": order.update_time.strftime("%Y-%m-%d %H:%M:%S")  # 评论创建时间
            }
            comments.append(comment)
        house_dict["img_url"] = img_url
        house_dict["facilities"] = facilities
        house_dict["comments"] = comments
        return house_dict


class Facility(BaseModel, db.Model):
    """设施信息模型类"""

    __tablename__ = "ih_facility_info"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)


class HouseImage(BaseModel, db.Model):
    """房屋图片模型类"""

    __tablename__ = "ih_house_image"

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house_info.id"), nullable=False)  # 图片表示的房屋编号
    url = db.Column(db.String(256), nullable=False)  # 图片的路径


class Order(BaseModel, db.Model):
    """订单模型类"""

    __tablename__ = "ih_order_info"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False)  # 创建订单的用户编号
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house_info.id"), nullable=False)   # 预订的房屋编号
    begin_date = db.Column(db.DateTime, nullable=False)    # 预订的起始时间
    end_date = db.Column(db.DateTime, nullable=False)      # 预订的结束时间
    days = db.Column(db.Integer, nullable=False)           # 预订的总天数
    house_price = db.Column(db.Integer, nullable=False)    # 房屋的单价
    amount = db.Column(db.Integer, nullable=False)         # 订单总金额
    status = db.Column(  # 订单的状态
        db.Enum(
            "WAIT_ACCEPT",  # 待接单
            "WAIT_PAYMENT", # 待支付
            "PAID",         # 已支付
            "WAIT_COMMENT", # 待评价
            "COMPLETE",     # 已完成
            "CANCELED",     # 已取消
            "REJECTED"      # 已拒单
        ),
        default="WAIT_ACCEPT", index=True
    )
    comment = db.Column(db.Text)  # 订单的评论或者拒单原因，根据订单的状态区分






























