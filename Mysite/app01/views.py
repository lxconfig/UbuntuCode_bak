# pylint: disable=no-member

from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# Create your views here.

def add_class(request):
    boys = [
            models.Boy(nickname = "徐峥", username = "徐峥", password = "123"),
            models.Boy(nickname = "黄渤", username = "黄渤", password = "123"),
            models.Boy(nickname = "王宝强", username = "王宝强", password = "123"),
            models.Boy(nickname = "周星驰", username = "周星驰", password = "123"),
    ]
    
    girls = [
            models.Girl(nickname = "马蓉", username = "马蓉", password = "123"),
            models.Girl(nickname = "白百合", username = "白百合", password = "123"),
            models.Girl(nickname = "巩俐", username = "巩俐", password = "123"),
            models.Girl(nickname = "张子文", username = "张子文", password = "123"),
    ]

    models.Boy.objects.bulk_create(boys)
    models.Girl.objects.bulk_create(girls)

    models.Love.objects.create(boy_id=1, girl_id=1)
    models.Love.objects.create(boy_id=1, girl_id=2)
    models.Love.objects.create(boy_id=1, girl_id=3)
    models.Love.objects.create(boy_id=2, girl_id=1)
    models.Love.objects.create(boy_id=2, girl_id=4)
    models.Love.objects.create(boy_id=3, girl_id=2)


    return HttpResponse("ok")


def boyInfo(request):
    """
    查某个单表的数据
    """
    boys = models.Boy.objects.all()
    print(boys)
    for row in boys:
        print(row.nickname)
    return HttpResponse("ok")


def boy_to_girl(request):
    """
    有第三张表的情况下。查询和某个男生有关系的女生信息
    定义：
        男生查女生是正向操作
        女生查男生是反向操作
        xxx是Boy/Girl类对象
        lists = xxx.love_set.all()
        for row in lists:
            print(row.girl.username)
    """

    """
    从Boy表出发，先连接Love表，再通过Love表连接Girl表

    # 一定要加first，否则是一个QuerySet，不能跨表
    xz = models.Boy.objects.filter(id=1).first()
    print(xz)  # 此时是Boy类对象
    # QuerySet[<Love: Love object (1)>, <Love: Love object (2)>, <Love: Love object (3)>]
    love_list = xz.love_set.all()
    print(love_list)
    # row是Love类的对象
    for row in love_list:
        print(row.girl.username)
    """
    # 反向操作
    # mr = models.Girl.objects.filter(id=1).first()
    # loves = mr.love_set.all()
    # print(loves)
    # for rows in loves:
    #     print(rows.boy.nickname)
    
    """
    从Love表出发，连接Boy表(Girl表)，再取数据时，连接另一张表
    
    love_list = models.Love.objects.filter(boy__id=2)
    print(love_list)
    for row in love_list:
        print(row.girl.username)
    """

    """
    从Love表出发，查询时直接连接Boy表和Girl表
    values不仅能把数据变成字典的格式，还能选择查询哪些字段
    values_list同理
    此外，还可以通过select_related来连接两张表
    """
    # love_list = models.Love.objects.filter(boy__nickname="王宝强").values("girl__id", "girl__username")   # 要做两次inner join
    # # love_list = models.Love.objects.filter(boy__nickname="王宝强").values_list("girl__id", "girl__username")
    # print(love_list.query)
    # for row in love_list:
    #     print(row)
    #     print(row["girl__id"])

    love_list = models.Love.objects.filter(boy__id=1).select_related("girl")   # 只做一次inner join Girl(通过where筛选出来boy=1的数据)
    print(love_list.query)
    for row in love_list:
        print(row.girl.username)


    return HttpResponse("ok")


def boy_to_girl_manytomanyfield(request):
    """
    通过ManyToManyField生成第三张表，此时没有第三表的模型类，仅有girl字段
    """

    """
    查和某个男生关联的女生(正向操作)   xxxx.字段名.all()
    """
    xz = models.Boy.objects.filter(id=1).first()
    print(xz.girl)   # app01.Girl.None
    print(xz.girl.all())  # QuerySet 其中都是Girl类的对象
    print(xz.girl.filter(id=2))  # 由于是QuerySet，所以可以继续filter筛选
    girl_list = xz.girl.all()
    for row in girl_list:
        print(row.nickname)
    

    """
    查和某个女生关联的男生(反向操作)  xxx.表名_set.all()
    """
    mr = models.Girl.objects.filter(id=1).first()
    print(mr.boy_set)  # app01.Boy.None
    print(mr.boy_set.all())  # QuerySet 其中都是Boy类的对象
    for row in mr.boy_set.all():
        print(row.nickname)

    return HttpResponse("ok")


def u2u(request):
    # models.U2U.objects.create(boy_id=1, girl_id=4)
    # models.U2U.objects.create(boy_id=1, girl_id=5)
    # models.U2U.objects.create(boy_id=1, girl_id=6)
    # models.U2U.objects.create(boy_id=2, girl_id=5)
    # models.U2U.objects.create(boy_id=2, girl_id=6)
    # xz = models.UserInfo.objects.filter(gender=1, id=1)
    # mr = models.UserInfo.objects.filter(gender=2, id=4)
    # models.U2U.objects.create(boy=xz, girl=mr)  # 可以写对象
    # objs = [
    #     models.UserInfo(nickname="徐峥", username="xz", gender=1),
    #     models.UserInfo(nickname="黄渤", username="hb", gender=1),
    #     models.UserInfo(nickname="张一山", username="zys", gender=1),
    #     models.UserInfo(nickname="马蓉", username="mr", gender=2),
    #     models.UserInfo(nickname="白百合", username="bbh", gender=2),
    #     models.UserInfo(nickname="小雨", username="xy", gender=2),
    # ]
    # models.UserInfo.objects.bulk_create(objs)

    """
    查和某个男生关联的女生
    """
    xz = models.UserInfo.objects.filter(gender=1, id=1).first()
    print(xz.girls.all())  # QuerySet  都是U2U对象
    # 所以还要在进行一次关联
    u2u_list = xz.girls.all()
    for row in u2u_list:
        print(row.girl.nickname)
    
    """
    查和某个女生关联的男生
    """
    mr = models.UserInfo.objects.filter(gender=2, id=4).first()
    print(mr.boys.all())  # QuerySet  都是U2U对象
    u2u_list = mr.boys.all()
    for row in u2u_list:
        print(row.boy.nickname)

    return HttpResponse("ok")


def self_association(request):
    """ManyToManyField自关联的情况
    """
    
    """
    查和某个男生有关联的女生
    """
    xz = models.UserInfo.objects.filter(id=1).first()
    for row in xz.m.all():
        print(row.nickname)
    
    """
    查和某个女生有关联的男生
    """
    mr = models.UserInfo.objects.filter(id=4).first()
    # print(mr.userinfo_set.all()
    for row in mr.userinfo_set.all():
        print(row.nickname)
    
    return HttpResponse("ok")


from django.forms import Form, fields

class LoginForm(Form):
    username = fields.CharField(max_length=16, min_length=6, required=True, error_messages={"required": "用户名不能为空"})
    password = fields.CharField(min_length=10, required=True)
    

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        obj = LoginForm(request.POST)
        if obj.is_valid():
            # 验证通过, 打印验证成功的数据, 是一个字典类型的数据
            print(obj.cleaned_data)
            return redirect("http://www.baidu.com")
        else:
            # 验证失败, 打印错误信息
            # errors实际上是对象(实现了__str__方法), 将所有错误信息都输出
            # print(obj.errors)
            # 某个字段可能验证规则很多，比如username有最长、最短、是否为空。可以只输出第一条错误
            print(obj.errors["username"][0])
            print(obj.errors["password"][0])
            return render(request, "login.html", {"obj": obj})