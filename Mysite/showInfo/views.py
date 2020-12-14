 # pylint: disable=no-member

from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.core.paginator import Paginator, Page
from showInfo.models import UserGroup, UserInfo, Boy, Girl, Male, Female, M2F
import pymysql, json

# Create your views here.

def showUserInfoFromDB(request):
    
    # 连接数据库
    conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")

    # 建立游标
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

    # 写sql语句,并执行
    sql = "select * from student"
    cursor.execute(sql)  # 返回受影响的行数

    # 拿一条结果
    ret = cursor.fetchall()
    # print(ret)

    # 关闭游标和连接
    cursor.close()
    conn.close()

    lists = [1,2,3]
    return render(request, "showinfo.html", {"infos": ret, "lists": lists})


def classes(request):
    tk = request.COOKIES.get("ticket")
    # tk = request.get_signed_cookie("ticket", salt="django")
    if not tk:
        return redirect("/show/login")
    # 连接数据库
    conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    sql = "select * from class"
    cursor.execute(sql)
    ret = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, "classes.html", {"classes": ret})


def add_class(request):
    if request.method == "POST":
        class_name = request.POST.get("name")
        conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")
        cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
        sql = "insert into class(caption) values(%s)"
        cursor.execute(sql, class_name)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/show/classes")
    else:
        return render(request, "add_class.html")


def modal_add_class(request):
    class_name = request.POST.get("name")
    if class_name:
        sqlhelper.modify("insert into class(caption) values(%s)", [class_name])
        return HttpResponse("OK")
        # return redirect("/show/classes")
    else:
        return HttpResponse("班级名称不能为空!")


def modal_edit_class(request):
    ret = {'status': True, "errormsg": None}
    try:
        nid = request.POST.get("nid")
        title = request.POST.get("title")
        sqlhelper.modify("update class set caption=%s where cid=%s", [title, nid])
    except Exception as e:
        ret['status'] = False
        ret['errormsg'] = str(e)
    ret = json.dumps(ret)
    return HttpResponse(ret)


def del_class(request):
    nid = request.GET.get("nid")
    conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    sql = "delete from class where cid = %s"
    cursor.execute(sql, nid)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/show/classes")


def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get("nid")
        conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")
        cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
        sql = "select cid, caption from class where cid = %s"
        cursor.execute(sql, nid)
        ret = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request, "edit_class.html", {"ret": ret})
    
    else:
        nid = request.POST.get("nid")
        name = request.POST.get("name")
        conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")
        cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
        sql = "update class set cid = %s, caption = %s where cid = %s"
        cursor.execute(sql, [nid, name, nid])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/show/classes")


from utilis import sqlhelper
def students(request):
    students_list = sqlhelper.get_list("select student.sid, student.sname, student.gender, student.class_id, class.caption from student left join class on student.class_id=class.cid", [])
    class_list = sqlhelper.get_list("select * from class", [])
    return render(request, "students.html", {"students_list": students_list, "class_list": class_list})


def add_student(request):
    if request.method == "GET":
        class_list = sqlhelper.get_list("select * from class", [])
        return render(request, "add_student.html", {"class_list": class_list})
    else:
        name = request.POST.get("name")
        class_id = request.POST.get("class_id")
        gender = request.POST.get("gender")
        sqlhelper.modify("insert into student(class_id, sname, gender) values(%s, %s, %s)", [class_id, name, gender])
        return redirect("/show/students")


def ajax_add_student(request):
    ret = {'status': True, "errormsg": None}
    try:
        name = request.POST.get("name")
        class_id = request.POST.get("class_id")
        gender = request.POST.get("gender")
        sqlhelper.modify("insert into student(sname, gender, class_id) values(%s, %s, %s)", [name, gender, class_id])
    except Exception as e:
        ret["status"] = True
        ret["errormsg"] = str(e)
    ret = json.dumps(ret)
    return HttpResponse(ret)


def edit_student(request):
    if request.method == "GET":
        student_id = request.GET.get("student_id")
        student_info = sqlhelper.get_one("select * from student where sid=%s", [student_id])
        class_list = sqlhelper.get_list("select * from class", [])
        return render(request, "edit_student.html", {"student_info": student_info, "class_list": class_list})
    else:
        name = request.POST.get("name")
        class_id = request.POST.get("class_id")
        student_id = request.GET.get("student_id")
        sqlhelper.modify("update student set sname=%s, class_id=%s where sid=%s", [name, class_id, student_id])
        return redirect("/show/students")


def ajax_edit_student(request):
    ret = {'status': True, "errormsg": None}
    try:
        name = request.POST.get("name")
        student_id = request.POST.get("student_id")
        gender = request.POST.get("gender")
        class_id = request.POST.get("class_id")
        sqlhelper.modify("update student set sname=%s, gender=%s, class_id=%s where sid=%s", [name, gender, class_id, student_id])
    except Exception as e:
        ret["status"] = True
        ret["errormsg"] = str(e)
    ret = json.dumps(ret)
    return HttpResponse(ret)


def delete_student(request):
    student_id = request.GET.get("student_id")
    print(student_id)
    sqlhelper.modify("delete from student where sid=%s", [student_id])
    return redirect("/show/students")


def class2teacher(request):
    result = sqlhelper.get_list("""
    select class2teacher.id, teacher.tname, class.caption, teacher.tid as tid
    from class2teacher 
    left join class
    on class2teacher.class_id = class.cid
    left join teacher
    on class2teacher.teacher_id = teacher.tid
    """, [])
    ret = {}
    for info in result:
        tid = info.get("tid")
        if tid in ret:
            ret[tid]['captions'].append(info['caption'])
        else:
            ret[tid] = {"tid": info["tid"], "name": info["tname"], "captions": [info["caption"]]}
    
    return render(request, "class2teacher.html", {"ret": ret.values()})


def add_teacher(request):
    if request.method == "GET":
        class_list = sqlhelper.get_list("select * from class", [])
        return render(request, "add_teacher.html", {"class_list": class_list})
    else:
        obj = sqlhelper.SqlHelper()

        name = request.POST.get("name")
        teacher_id = obj.create("insert into teacher(tname) values(%s)", [name])

        class_id = request.POST.getlist("class_id")
        data_list = []
        for cid in class_id:
            tmp = (teacher_id, cid)
            data_list.append(tmp)
        # print(data_list)
        obj.multiple_modify("insert into class2teacher(teacher_id, class_id) values(%s, %s)", data_list)
        obj.close()
        return redirect("/show/class2teacher")


def edit_teacher(request):
    obj = sqlhelper.SqlHelper()
    if request.method == "GET":
        teacher_id = request.GET.get("tid")
        teacher_info = obj.get_one("select * from teacher where tid=%s", [teacher_id])
        teacher_class = obj.get_list("select class_id from class2teacher where teacher_id=%s", [teacher_id])   # 老师教授的班级号
        class_list = obj.get_list("select * from class", [])
        # print(teacher_info)
        # print(teacher_class)
        # print(class_list)
        temp = []
        for cid in teacher_class:
            temp.append(cid["class_id"])
        return render(request, "edit_teacher.html", {"class_list": class_list, "teacher_info": teacher_info, "teacher_class": temp})
    
    else:
        teacher_id = request.GET.get("tid")
        name = request.POST.get("name")
        class_ids = request.POST.getlist("class_ids")

        # 修改姓名
        obj.modify("update teacher set tname=%s where tid=%s", [name, teacher_id])

        # 修改任教班级
        data_list = []
        for cid in class_ids:
            tmp = (teacher_id, cid)
            data_list.append(tmp)
        obj.modify("delete from class2teacher where teacher_id=%s", [teacher_id])
        obj.multiple_modify("insert into class2teacher(teacher_id, class_id) values(%s, %s)", data_list)

        return redirect("/show/class2teacher")


def get_all_class(request):
    import time
    time.sleep(3)
    obj = sqlhelper.SqlHelper()
    class_list = obj.get_list("select cid, caption from class", [])
    obj.close()
    return HttpResponse(json.dumps(class_list))


def modal_add_teacher(request):
    ret = {"status": True, "errorMsg": None}
    try:
        name = request.POST.get("name")
        class_ids = request.POST.getlist("class_ids")
        obj = sqlhelper.SqlHelper()
        teacher_id = obj.create('insert into teacher(tname) values(%s)', [name])
        
        data_list = []
        for cid in class_ids:
            tmp = (teacher_id, cid)
            data_list.append(tmp)
        
        obj.multiple_modify("insert into class2teacher(teacher_id, class_id) values(%s, %s)", data_list)
    except Exception as e:
        ret["status"] = False
        ret["errorMsg"] = str(e)
    return HttpResponse(json.dumps(ret))


def test(request):
    return render(request, "layout.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        if name == "lx" and pwd == "123":
            obj = redirect("/show/classes")
            # obj.set_cookie("ticket", name)
            obj.set_signed_cookie("ticket", name, salt="django")   # 签名版cookie
            return obj
        else:
            return redirect("/show/login")


def index(request):
    # print(num)
    u = request.session.get("user")
    if u:
        return HttpResponse("OKKKKK! %s" % u)
    else:
        return redirect("/session_login")


def index2(request, nid):
    print(nid)
    return HttpResponse("OKKKKK!")


def CRUD(request):
    # 增
    # UserGroup.objects.create(title="销售部")
    # UserGroup.objects.create(title="开发部")
    # UserInfo.objects.create(user="alex", password="123", age=18, fk_id=1)
    # UserInfo.objects.create(user="eric", password="123", age=18, fk_id=2)
    # UserInfo.objects.create(user="geek", password="123", age=18, fk_id=3)
    # UserInfo.objects.create(user="hank", password="123", age=18, fk_id=3)
    # UserInfo.objects.create(user="brown", password="123", age=18, fk_id=2)
    # UserInfo.objects.create(user="jims", password="123", age=18, fk_id=2)
    
    # 删
    # UserGroup.objects.filter(id=1).delete()

    # 改
    # UserGroup.objects.filter(id=1).update(title="销售1部")

    # 查 QuerySet类的对象
    group_list = UserGroup.objects.all()

    # return HttpResponse("ok")
    return render(request, "crud.html", {"group_list": group_list})


class CBV(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        print(request.POST.get("username"))
        return HttpResponse("CBV.post")


def foreign(request):
    # 多查一
    # result = UserInfo.objects.all()
    # for row in result:
    #     print(row.nid, row.user, row.password, row.age, row.fk.title)
    
    # 一查多
    # result = UserGroup.objects.all()  # QuerySet[obj,obj,obj]
    # for row in result:
    #     for users in row.userinfo_set.all():
    #         print(row.id, row.title, users.nid, users.user)

    # 查询数据时，三种返回数据的格式
    # 1. obj对象  QuerySet[obj,obj,obj]
    # result = UserGroup.objects.all()

    # 2. 字典  QuerySet[{"id":1, "name":"xx"}]
    # values()指定取几列
    # 可以在设置字段时连表  外键字段__一类字段
    # result = UserInfo.objects.all().values("nid", "user", "fk__title")
    result = UserGroup.objects.all().values("id", "title")
    # result = UserGroup.objects.values("id", "title", "userinfo", "userinfo__user")
    # result = UserGroup.objects.values_list("id", "title", "userinfo", "userinfo__age")
    print(result)
    
    # 3. 元组  QuerySet[(1, "xx"), (2, "sss")]
    # 同样可以在设置字段时连表
    # result = UserInfo.objects.all().values_list("nid", "user", "fk__title")
    # print(result)

    return HttpResponse("ok")


def paging(request):
    # for i in range(300):
    #     user = "root" + str(i)
    #     UserInfo.objects.create(user=user, age=18, password="123", fk_id=3)
    current_page = request.GET.get("page")
    user_list = UserInfo.objects.all()

    # 先创建Paginator类的对象
    paginator = Paginator(user_list, 10)

    # print(paginator.per_page)
    # print(paginator.count)
    # print(paginator.num_pages)
    # print(paginator.page_range)

    # 然后获取指定页数的数据
    try:
        posts = paginator.page(current_page)
    except Exception:
        posts = paginator.page(1)

    return render(request, "paging.html", {"posts": posts})


from utilis.pager import Pager

def custom(request):
    """自定义分页
    """
    all_datas_num = UserInfo.objects.all().count()
    page_info = Pager(request.GET.get("page"), 10, all_datas_num, "/custom")
    
    user_list = UserInfo.objects.all()[page_info.start(): page_info.end()]


    return render(request, "custom.html", {"user_list": user_list, "page_info": page_info})



def many2many(request):
    """多对多关系
    """
    # obj = [
    #     Boy(name="alex"),
    #     Boy(name="eric"),
    #     Boy(name="mike"),
    #     Boy(name="tom"),
    #     Boy(name="jock"),
    # ]
    # Boy.objects.bulk_create(obj, 5)
    # obj = [
    #     Girl(nick="jone"),
    #     Girl(nick="jane"),
    #     Girl(nick="hike"),
    #     Girl(nick="jim"),
    # ]
    # Girl.objects.bulk_create(obj, 5)

    # Love.objects.create(boy_id=1, girl_id=2)
    # Love.objects.create(boy_id=1, girl_id=3)
    # Love.objects.create(boy_id=2, girl_id=3)
    # Love.objects.create(boy_id=2, girl_id=4)

    # boy = Boy.objects.filter(name="alex").first()
    # love_list = boy.love_set.all()
    # for row in love_list:
    #     print(row.girl.nick)    # 每次都再发一次sql请求，用于连Girl表
    
    # love_list = Love.objects.filter(boy__name="alex")   # 查询时连Boy表
    # for row in love_list:
    #     print(row.girl.nick)   # 取数据时，再连Girl表

    # love_list = Love.objects.filter(boy__name="alex").values("girl__nick")  # 查询时直接连两张表, [{}, {}]
    # print(love_list.query)
    # for row in love_list:
    #     print(row["girl__nick"])

    # love_list = Love.objects.filter(boy__name="eric").select_related("girl")  # 查询时直接连两张表, [obj, obj]
    # print(love_list.query)
    # for row in love_list:
    #     print(row.girl.nick)

    # 多对多关系，不手动创建第三张表的写法
    # obj = Boy.objects.filter(name="eric").first()
    # print(obj.id, obj.name)

    """ 对第三张表的数据进行操作 """
    # 从Boy类出发，找Girl类的数据
    # 1. 增
    # obj.m.add(2)   # 用obj.id当作boy.id的值
    # obj.m.add(1,3)
    # obj.m.add(*[1, 3])

    # 2. 删
    # obj.m.remove(1)
    # obj.m.remove(2, 3)
    # obj.m.remove(*[2])

    # 3. 重置
    # obj.m.set([1])

    # 4. 查
    # girl_list = obj.m.all()   # 拿到的是Girl类的对象
    # a = obj.m.filter(nick="jone")   # 可以按条件继续筛选
    # print(a)
    # for row in girl_list:
    #     print(row.nick)
    
    # obj.m.clear()   # 把和obj相关的全部删掉

    """ 反向操作 """
    # 从Girl类出发，找Boy类的数据
    obj = Girl.objects.filter(nick="jone").first()
    print(obj.id, obj.nick)
    print(obj.boy_set.all())   # 拿到和obj相关联的Boy类数据

    for row in obj.boy_set.all():
        print(row.id, row.name)

    return HttpResponse("okkkk")



def filters(request):
    return render(request, "filters.html", {"name": "ALEX"})



def session_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        u = request.POST.get("username")
        p = request.POST.get("password")
        if u == "lx" and p == '123':
            # 1. 生成随机字符串
            # 2. 通过cookie发送给客户端
            # 3. 服务端保存(在数据库中)
            request.session["user"] = "lx"
            return redirect("/index")
        else:
            return redirect("/show/login")


def male_female_login(request):
    if request.method == "GET":
        return render(request, "male_female_login.html")
    else:
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        rmb = request.POST.get("rmb")
        gender = request.POST.get("gender")
        if gender == "1":
            obj  = Male.objects.filter(username=user, password=pwd).first()
        else:
            obj  = Female.objects.filter(username=user, password=pwd).first()
        
        if not obj: return render(request, "male_female_login.html", {"msg": "用户名或密码错误"})
        # request.session["user_id"] = obj.id
        # request.session["username"] = user
        # request.session["gender"] = gender
        request.session["user_info"] = {"user_id": obj.id, "username": user, "gender": gender, "nickname": obj.nickname}
        return redirect("/male_female_info")

def male_female_info(request):
    if not request.session.get("user_info"):
        return redirect("/login")
    else:
        gender = request.session.get("user_info").get("gender")
        if gender == "1":
            # 男生
            user_list = Female.objects.all()
        else:
            user_list = Male.objects.all()
    return render(request, "male_female_info.html", {"user_list": user_list})


# def add_data(request):
#     Male.objects.create(nickname="张三", username="zhangsan", password="123")
#     Male.objects.create(nickname="李四", username="lisi", password="123")
#     Male.objects.create(nickname="王五", username="wangwu", password="123")

#     Female.objects.create(nickname="翠花", username="cuihua", password="123")
#     Female.objects.create(nickname="小楼", username="xiaolou", password="123")
#     Female.objects.create(nickname="小雨", username="xiaoyu", password="123")
#     Female.objects.create(nickname="小米", username="xiaomi", password="123")

    # M2F.objects.create(male_id=1, fmale_id=1)
    # M2F.objects.create(male_id=1, fmale_id=2)
    # M2F.objects.create(male_id=1, fmale_id=3)
    # return HttpResponse('ok')

def logout(request):
    request.session.clear()   # 删除cookie
    # request.session.delete(request.session.session_key)    #  数据库删除
    return redirect("/login")


def others(request):
    current_user_id = request.session.get("user_info").get("user_id")
    gender = request.session.get("user_info").get("gender")
    if gender == "1":
        user_list = M2F.objects.filter(male=current_user_id).values("fmale__nickname")
    else:
        user_list = M2F.objects.filter(female=current_user_id).values("male__nickname")
    return render(request, "others.html", {"user_list": user_list})