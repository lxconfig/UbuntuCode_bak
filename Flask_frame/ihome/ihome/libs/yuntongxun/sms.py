
from .CCPRestSDK import REST
import ssl

# 取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

ssl.match_hostname = lambda cert, hostname: True

# 主帐号
accountSid = '8a216da870e2267e01714370cf4a33ea'

# 主帐号Token
accountToken = '3ad79c7cdc794addad5c4b82d3fad6d1'

# 应用Id
appId = '8a216da870e2267e01714370cfaa33f1'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为列表 例如：['12','34']，如不需替换请填 ''
  # @param $tempId 模板Id


class CCP:
    """自己封装的发送短信的辅助类"""
    # 单例模式,防止REST SDK被多次初始化
    instance = None  # 用来保存对象的类属性
    def __new__(cls):
        if cls.instance is None:
            # 说明还没有创建对象，则调用父类创建一个
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP,serverPort,softVersion)
            obj.rest.setAccount(accountSid,accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj
        return cls.instance
    
    def send_template_sms(self, to, datas, temp_id):

        result = self.rest.sendTemplateSMS(to,datas,temp_id)
        for k,v in result.items(): 
            if k == 'templateSMS' :
                for k,s in v.items(): 
                    print('%s:%s' % (k, s))
            else:
                print('%s:%s' % (k, v))
        # statusCode:000000
        # smsMessageSid:6d4e9cdc9e5848ebb3fdf06b3c27bfbe
        # dateCreated:20200404132947
        
        # 给视图函数返回结果
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 发送成功
            return 0
        else:
            # 发送失败
            return -1


if __name__ == "__main__":
    ccp = CCP()
    ccp.send_template_sms("18370850448", ["1234", "5"], 1)
   