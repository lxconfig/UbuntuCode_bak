from ronglian_sms_sdk import SmsSDK

accId = '8a216da870e2267e01714370cf4a33ea'
accToken = '3ad79c7cdc794addad5c4b82d3fad6d1'
appId = '8a216da870e2267e01714370cfaa33f1'

def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = '18370850448'
    datas = ("1234", '5')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)

send_message()