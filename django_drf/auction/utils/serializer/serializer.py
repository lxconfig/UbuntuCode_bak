import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django_redis import get_redis_connection


def phone_validator(value):
    """对手机号格式增加额外的判断
    若合法 返回空即可
    若不合法 引发一个异常返回即可
    """
    if not re.match(r"^1([3|4|5|6|7|8|9])\d{9}$", value):
        raise ValidationError("手机号格式错误")

def code_validator(value):
    if not re.match(r"^\d{4}$", value):
        raise ValidationError("验证码格式错误")


class MessageSerializer(serializers.Serializer):
    """帮助做手机号验证
    默认只会判断是否为空
    """
    phone = serializers.CharField(label="手机号", validators=[phone_validator, ])

class LoginSerializer(serializers.Serializer):
    """帮助做手机号和验证码验证
    默认只会判断是否为空
    """
    phone = serializers.CharField(label="手机号", validators=[phone_validator, ])
    code = serializers.CharField(label="验证码", validators=[code_validator, ])

    def validate_code(self, value):
        """钩子函数，对code进行验证
        """
        if len(value) != 4:
            raise ValidationError("验证码格式错误")
        if not value.isdecimal():
            raise ValidationError("验证码格式错误")
        phone = self.initial_data.get("phone")
        conn =get_redis_connection()
        code = conn.get(phone)
        if not code:
            raise ValidationError("验证码过期")
        if value != code.decode("utf-8"):
            raise ValidationError("验证码错误")
        # 验证通过
        return value

