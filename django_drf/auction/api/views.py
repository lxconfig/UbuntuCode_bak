import random
import uuid


from utils.ronglianyun.msg import send_message
from utils.serializer.serializer import MessageSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django_redis import get_redis_connection

from django.shortcuts import render
from api.models import UserInfo



class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # 1. 获取手机号，验证码
        phone = request.data["phone"]
        code = request.data["code"]
        print(phone, code)
        # 2. 手机号，验证码格式校验
        ser = LoginSerializer(data=request.data)
        # 这里已经通过钩子函数对code进行过验证
        if not ser.is_valid():
            return Response({
                "status": False,
                "message": "手机号或验证码错误"
            })
        # 3. 再数据库中获取用户信息（获取/创建）
        phone = ser.validated_data.get("phone")
        # 若phone存在于数据库中，就get这条数据
        # 若不在，就用这个phone创建一条数据
        user_obj, flag = UserInfo.objects.get_or_create(phone=phone)
        user_obj.token = str(uuid.uuid4())
        user_obj.save()
        # 4. 返回结果
        return Response({
                "status": True,
                "data": {
                    "token": user_obj.token,
                    "phone": phone
                }
            })

class message(APIView):
    def get(self, request, *args, **kwargs):
        # 1. 获取手机号
        phone = request.query_params.get("phone")
        # 2. 手机号格式校验
        ser = MessageSerializer(data=request.query_params)
        if not ser.is_valid():
            return Response({
                "status": False,
                "message": "手机格式错误"
            })
        # 得到匹配完成的数据
        phone = ser.validated_data.get("phone")

        # 3. 生成随机验证码
        random_code = random.randint(1000, 9999)
        print(random_code)

        # 4. 发送到手机上
        """
        send_message(phone, random_code, "1")
        """

        # 5. 保存验证码 + 手机号
        conn = get_redis_connection()
        conn.set(phone, random_code, ex=30)
        return Response({
            "status": True,
            "message": "发送成功"
            })
