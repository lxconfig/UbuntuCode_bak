
from . import api
from ihome.utilis.commons import login_required
from flask import g, jsonify, current_app, request, session
from ihome.utilis.response_code import RET
from ihome.models import User, Area, House, Facility, HouseImage, Order
from ihome.utilis.image_storage import storage
from ihome import db, constants, redis_store
from ihome.utilis.image_storage import storage
from datetime import datetime
import json


@api.route("/areas")
def get_area_info():
    """获取城区信息"""
    # 尝试从redis中读取信息
    try:
        resp_json = redis_store.get("area_info")
    except Exception as e:
        current_app.logger.error(e)
    else:
        if resp_json is not None:
            # 有缓存数据，直接返回
            current_app.logger.info("hit the redis area_info")
            return resp_json.decode("utf-8"), 200, {"Content-Type": "application/json"}
    try:
        areas = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")
    
    # 将areas列表(值为对象)转为字典
    area_dict = []
    for area in areas:
        # 一般把转为字典的方法定义在类中
        area_dict.append(area.to_dict())
    
    # 将查询出来的数据保存到redis中作为缓存cache
    # 继续使用string类型，并且要设置有效期,否则每次拿到的都是旧数据
    resp_dict = dict(errno=RET.OK, errmsg="查询成功", data=area_dict)
    resp_json = json.dumps(resp_dict)  # 转换成json格式数据，本质还是字符串
    try:
        redis_store.setex("area_info", constants.AREA_INFO_REDIS_CACHE_EXPIRES, resp_json)
    except Exception as e:
        current_app.logger.error(e)
    
    # 返回
    return resp_json, 200, {"Content-Type": "application/json"}



@api.route("/houses/info", methods=["POST"])
@login_required
def set_house_info():
    """发布新房源信息"""
    
    # 获取参数
    user_id = g.user_id
    house_data = request.get_json()
    title = house_data.get("title")
    price = house_data.get("price")
    area_id = house_data.get("area_id")
    address = house_data.get("address")
    room_count = house_data.get("room_count")
    acreage = house_data.get("acreage")
    unit = house_data.get("unit")
    capacity = house_data.get("capacity")
    beds = house_data.get("beds")
    deposit = house_data.get("deposit")
    min_days = house_data.get("min_days")
    max_days = house_data.get("max_days")

    # 校验参数
    if not all([title, price, area_id, address, room_count, acreage, unit, capacity, beds, deposit, max_days, min_days]):
        return jsonify(error=RET.PARAMERR, errmsg="参数不完整")

    # 判断金额是否正确
    try:
        price = int(float(price) * 100)   # 数据库中的单位是 分
        deposit = int(float(deposit) * 100)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.PARAMERR, errmsg="金额设置错误")
    
    # 判断城区id是否存在
    try:
        area = Area.query.get(area_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="数据库异常")
    if not area:
        return jsonify(error=RET.NODATA, errmsg="城区数据有误")
    
    # 保存房屋信息
    house = House(
        user_id=user_id,
        title=title,
        price=price,
        area_id=area_id,
        address=address,
        room_count=room_count,
        acreage=acreage,
        unit=unit,
        capacity=capacity,
        beds=beds,
        deposit=deposit,
        min_days=min_days,
        max_days=max_days
    )
    
    # 处理房屋的设施信息
    facility_ids = house_data.get("facility")

    # 先到数据库中验证
    if facility_ids:    # 设施信息不是必填，传过来的数据是列表形式的
        try:
            # 过滤出用户勾选了的设施
            facilities = Facility.query.filter(Facility.id.in_(facility_ids)).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(error=RET.DBERR, errmsg="数据库异常")
        if facilities:
            # 表示数据库中有对应设施的数据
            # 保存数据
            house.facilities = facilities   # 会自动将设施、房屋的信息添加到房屋设施表中
    try:
        db.session.add(house)
        db.session.commit()
    except Exception as e:
        db.session.rollback()   # 如果出错，之前的房屋信息也要回退，所以统一在这里回退
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="数据库异常")
    
    # 返回
    return jsonify(error=RET.OK, errmsg="保存数据成功", data={"house_id": house.id})  # 返回房屋id，方便提交图片时使用



@api.route("/houses/images", methods=["POST"])
@login_required
def set_house_image():
    """设置房屋的图片"""

    # 获取参数  图片  房屋id
    image_file = request.files.get("house_image")
    house_id = request.form.get("house_id")

    # 校验数据
    if not all([image_file, house_id]):
        return jsonify(erron=RET.PARAMERR, errmsg="参数填写不完整")
    
    # 判断房屋是否存在
    try:
        house = House.query.get(house_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(erron=RET.DBERR, errmsg="数据库异常")
    
    if not house:
        # 没查到房屋信息
        return jsonify(erron=RET.NODATA, errmsg="房屋不存在")
    
    # 上传图片到七牛
    image_data = image_file.read()
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="保存图片失败")
    
    # 保存图片名字到数据库中
    house_image = HouseImage(house_id=house_id, url=file_name)
    db.session.add(house_image)

    # 处理房屋的主图片，这里选第一张上传的图片作为主图片
    if not house.index_image_url:
        house.index_image_url = file_name
        db.session.add(house)
    # 提交数据库
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存图片数据异常")
    
    # 返回
    image_url = constants.QINIU_URL_DOMAIN + file_name
    return jsonify(errno=RET.THIRDERR, errmsg="保存图片失败", data={"image_url": image_url})



@api.route("/users/houses", methods=["GET"])
@login_required
def show_users_houses_info():
    """展示用户自己的房屋信息"""
    # 获取参数
    user_id = g.user_id
    # 查询用户的房屋信息
    try:
        user = User.query.get(user_id)
        houses = user.houses   # 用户的房屋
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    houses_list = []

    if houses:
        # 这里的house是House类的对象
        for house in houses:
            houses_list.append(house.to_dict())
    return jsonify(errno=RET.OK, errmsg="OK", data={"houses": houses_list})


@api.route("/houses/index", methods=["GET"])
def get_house_index():
    """主页幻灯片展示房屋信息"""

    # 从redis中读取，缓存
    try:
        # 读取出来就是json格式
        house_data = redis_store.get("index_house_page")
    except Exception as e:
        current_app.logger.error(e)
    
    if house_data:
        # 有缓存
        current_app.logger.info("hit index house page redis")
        return '{"errno": 0, "errmsg": "OK", "data": %s}' % house_data.decode("utf-8"), 200, {"Content-Type": "application/json"}
    else:
        # 没有缓存

        # 从数据库中查询数据
        try:
            # 根据订单量查询数据，并限制读取条数
            houses = House.query.order_by(House.order_count.desc()).limit(constants.INDEX_PAGE_IMAGE_MAX)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="查询数据失败")
        
        houses_list = []   # [{}, {}, {}]
        if not houses:
            # 没有查询到数据
            return jsonify(errno=RET.NODATA, errmsg="查询无数据")
        
        for house in houses:
            if not house.index_image_url:
                # 房屋没有图片信息，则跳过
                continue
            houses_list.append(house.to_dict())
        
        # 将数据转为json，保存到redis中做缓存
        house_data = json.dumps(houses_list)
        try:
            redis_store.setex("index_house_page", constants.HOME_PAGE_REDIS_EXPIRES, house_data)
        except Exception as e:
            current_app.logger.error(e)
        
        # 返回
        return '{"errno": 0, "errmsg": "OK", "data": %s}' % house_data, 200, {"Content-Type": "application/json"}



@api.route("/houses/<int:house_id>")
def get_house_info(house_id):
    """获取房屋的详细信息"""
    # 获取参数   用户id, 房屋id
    user_id = session.get("user_id", '-1')   # 不存在user_id时设置一个默认值，方便前端判断，当没有user_id时，表示不是房东，不能显示 预定 按钮

    # 先读取redis缓存
    try:
        house_json_data = redis_store.get("house_info_%s" % house_id)
    except Exception as e:
        current_app.logger.error(e)
    
    if house_json_data:
        return '{"errno": "0", "errmsg": "OK", "data":{"user_id": %s, "house": %s}}' % (user_id, house_json_data), 200, {"Content-Type": "application/json"}

    # 判断房屋id是否存在
    try:
        house = House.query.get(house_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")
    
    if not house:
        return jsonify(errno=RET.NODATA, errmsg="房屋信息不存在")
    
    # 将房屋对象转换为字典
    try:
        house_data = house.full_to_dict()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据出错")
    
    # 保存到redis中做缓存数据
    house_json_data = json.dumps(house_data)
    try:
        redis_store.setex("house_info_%s" % house_id, constants.HOUSE_DETAIL_REDIS_EXPIRES, house_json_data)
    except Exception as e:
        current_app.logger.error(e)
    
    # 返回
    return '{"errno": "0", "errmsg": "OK", "data":{"user_id": %s, "house": %s}}' % (user_id, house_json_data), 200, {"Content-Type": "application/json"}



# /api/v1.0/houses?sd=2020-04-13&ed=2020-04-14&aid=1&sk=new&p=1
@api.route("/houses")
def get_houses_list():
    """获取房屋信息列表页(搜索页)"""
    # 获取参数
    start_date = request.args.get("sd", "")   # 开始日期
    end_date = request.args.get("ed", "")     # 结束日期
    area_id = request.args.get("aid", "")     # 区域编号
    sorted_key = request.args.get("sk", "new")   # 排序方式, 默认以new方式排序
    page = request.args.get("page")          # 页数

    # 转换成日期形式，并判断是否合法
    try:
        if start_date:
            start_date = datetime.strptime("%Y-%m-%d")
        if end_date:
            end_date = datetime.strptime("%Y-%m-%d")
        if start_date and end_date:
            # 当两个日期都存在时，判断开始日期是否小于结束日期
            assert start_date <= end_date
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="日期参数错误")
    
    # 判断区域编号是否存在
    if area_id:
        try:
            area = Area.query.get(area_id)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.PARAMERR, errmsg="区域参数错误")
        if not area:
            return jsonify(errno=RET.NODATA, errmsg="区域不存在")
    
    # 判断页数是否是数字
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1     # 默认设置为第一页
    
    # 先再redis中查询缓存数据
    redis_hash_key = "house_index_%s_%s_%s_%s" % (start_date, end_date, area_id, sorted_key)
    try:
        resp_json = redis_store.hget(redis_hash_key, page)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if resp_json:
            return resp_json, 200, {"Content-Type": "application/json"}

    # 由于查询的参数多，并且可能有的有，有的没有，所以使用*拆包的方法来做
    filter_params = []   # 存放过滤条件的列表

    # 填充该列表
    # 时间条件
    conflict_orders = None
    try:
        if start_date and end_date:
            # 查询冲突的订单
            conflict_orders = Order.query.filter(Order.begin_date <= end_date, Order.end_date >= start_date).all()    # 在时间上冲突的订单
        elif start_date:
            conflict_orders = Order.query.filter(Order.end_date >= start_date).all()    # 在时间上冲突的订单
        elif end_date:
            conflict_orders = Order.query.filter(Order.begin_date <= end_date).all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    if conflict_orders:
        # 获取这些冲突订单的房屋id
        conflict_orders_house_ids = [order.house_id for order in conflict_orders]
        if conflict_orders_house_ids:
            # 可能没有订单冲突,有冲突房屋id时在添加到过滤条件
            filter_params.append(House.id.notin_(conflict_orders_house_ids))   # 条件是：找到不存在时间冲突的房屋id(如果仅按时间过滤，那么会少掉那些没有过订单的房屋)
    
    # 区域条件
    if area_id:
        # ==号实际上是调用对象的__eq__()方法，只不过sqlalchemy重写了这个方法，使得返回值不是True或者False
        # [<sqlalchemy.sql.elements.BinaryExpression object at 0x0000023E1BC40278>]
        filter_params.append(House.area_id == area_id)  

    # 查询数据库，在按排序关键字sk排序
    if sorted_key == "booking":   # 订单量 (入住最多)
        house_query = House.query.filter(*filter_params).order_by(House.order_count.desc())  # 此时还没有查询数据，house_query只是sql语句
    elif sorted_key == "price-inc":  # 价格升序
        house_query = House.query.filter(*filter_params).order_by(House.price.asc())
    elif sorted_key == "price-des":  # 价格降序
        house_query = House.query.filter(*filter_params).order_by(House.price.desc())
    else:
        house_query = House.query.filter(*filter_params).order_by(House.create_time.desc())   # 默认按新旧顺序

    # 处理分页   参数：当前页数, 每页的数据量, 出错时输出404
    # page_obj是一个分页对象  <flask_sqlalchemy.Pagination object at 0x000001E63F160E48>
    try:
        page_obj = house_query.paginate(page=page, per_page=constants.HOUSE_LIST_PAGE_CAPACITY, error_out=False)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    # 获取数据
    houses = []
    houses_list = page_obj.items  # 此时才真正查询数据库，获取到列表形式的数据  [<House 1>]
    for house in houses_list:
        houses.append(house.to_dict())
    
    # 获取总页数
    total_pages = page_obj.pages

    # 将每种条件组合成的查询结果保存为缓存记录
    resp_dict = dict(errno=RET.OK, errmsg="OK", data={"total_pages": total_pages, "houses": houses, "current_page": page})
    resp_json = json.dumps(resp_dict)

    if page <= total_pages:
        # 保存到redis中，使用hash类型
        redis_hash_key = "house_index_%s_%s_%s_%s" % (start_date, end_date, area_id, sorted_key)
        try:
            # redis_store.hset(redis_hash_key, page, resp_json)
            # 设置有效期
            # redis_store.expire(redis_hash_key, constants.HOUSE_LIST_PAGE_CACHE_EXPIRES)
            # 上面两条语句可能成功一条失败一条，所以采用pipeline来执行这两条命令
            pipeline = redis_store.pipeline()   # 创建pipeline管道对象,可以一次执行多条语句
            pipeline.multi()    # 开启多个语句
            pipeline.hset(redis_hash_key, page, resp_json)
            pipeline.expire(redis_hash_key, constants.HOUSE_LIST_PAGE_CACHE_EXPIRES)
            pipeline.execute()   # 执行语句

        except Exception as e:
            current_app.logger.error(e)
    # 返回
    return resp_json, 200, {"Content-Type": "application/json"}