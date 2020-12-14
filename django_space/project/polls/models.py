from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

"""
    类 -> 数据库表
    类字段 -> 表字段
    主键自动创建
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published ')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    choices_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # 外键字段 question_id
    quesition = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.choices_text