from django.db import models

# Create your models here.


class Boy(models.Model):
    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.IntegerField()

    # 通过ManyToManyField来完成多对多关系
    # 会生成一张表： 应用名_类名_字段名(app01_boy_girl)
    girl = models.ManyToManyField("Girl")


class Girl(models.Model):
    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.IntegerField()


# class Love(models.Model):
#     boy = models.ForeignKey("Boy", on_delete=models.DO_NOTHING)
#     girl = models.ForeignKey("Girl", on_delete=models.DO_NOTHING)


class UserInfo(models.Model):
    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.IntegerField(choices=gender_choices)

    # 自关联,会生成一张表 应用名_类名_字段名(app01_userinfo_m)
    # 这张表包含三个字段：
    # id, from_userinfo_id(假定为男生id), to_userinfo_id(假定为女生id)
    m = models.ManyToManyField("UserInfo")


class U2U(models.Model):
    """
    boy和girl代指的其实是Boy类和Girl类的对象
    related_name: 反向关联时，u2u_set.all  ==> boys.all()
    related_quert_name: u2u_set.all()  ===》 boys_set.all()
    """
    boy = models.ForeignKey("UserInfo", related_name="girls", on_delete=models.DO_NOTHING)
    girl = models.ForeignKey("UserInfo", related_name="boys", on_delete=models.DO_NOTHING)


class Comment(models.Model):
    """评论表
    外键字段的自关联
    """
    news_id = models.IntegerField()
    content = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    reply = models.ForeignKey("Comment", on_delete=models.DO_NOTHING, null=True, blank=True)   # 回复的评论id