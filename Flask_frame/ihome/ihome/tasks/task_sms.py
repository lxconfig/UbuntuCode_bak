
from ihome.libs.yuntongxun.sms import CCP
from celery import Celery


# 创建celery的工作对象
celery_app = Celery("task_sms", broker="redis://127.0.0.1:6379/1", backend="redis://127.0.0.1:6379/2")


# 定义任务
@celery_app.task
def send_sms(to, datas, temp_id):
    """发送短信的异步任务"""
    ccp = CCP()
    ccp.send_template_sms(to, datas, temp_id)