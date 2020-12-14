from django.db import models

# Create your models here.


class UserGroup(models.Model):
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    """默认表名是：应用名_类名(全小写)
    外键字段默认名字是： 字段名_id(小写)
    """
    nid = models.AutoField(primary_key=True)  # 可以不写，默认会添加整型的主键
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=1)
    fk = models.ForeignKey("UserGroup", null=True, on_delete=models.DO_NOTHING)


# 多对多关系
class Boy(models.Model):
    name = models.CharField(max_length=32)

    # 不会新建一个m的字段，而是新建一张表，其中记录着Boy和Girl的多对多关系
    # 表名就是 应用名_类名_字段名  showinfo_boy_m
    # 其中的字段包括 id, boy_id, girl_id(只能有这三列，不能加其他的列)
    m = models.ManyToManyField("Girl")

    # 还可以把ManyToManyField和Love类结合在一起使用
    # 可以清空数据clear()和查询数据obj.m.all()
    # m = models.ManyToManyField("Girl", through="Love", through_fields=("boy", "girl"))


class Girl(models.Model):
    nick = models.CharField(max_length=32)
    # m = models.ManyToManyField("Boy")   # 也可以创建在这里


"""事实上，第三张表可以不用手动创建，可以让Django帮我们创建"""
# class Love(models.Model): 
#     boy = models.ForeignKey("Boy", on_delete=models.DO_NOTHING)
#     girl = models.ForeignKey("Girl", on_delete=models.DO_NOTHING)

    # 创建联合唯一索引
    # class Meta:
    #     unique_together = [
    #         ("boy", "girl"),
    #     ]


class Test(models.Model):
    nid = models.IntegerField(
        verbose_name="编号",
        blank=True,
        help_text="用户编号",
        error_messages={"null": "编号为空"},
        primary_key=True,
        null=False,
    )
    name = models.CharField(
        null=True,
        default="zhangsan",
        max_length=32,
    )


class Male(models.Model):
    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class Female(models.Model):
    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class M2F(models.Model):
    male = models.ForeignKey("Male", on_delete=models.DO_NOTHING)
    fmale = models.ForeignKey("Female", on_delete=models.DO_NOTHING)