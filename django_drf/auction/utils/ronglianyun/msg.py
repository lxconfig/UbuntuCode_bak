from ronglian_sms_sdk import SmsSDK

accId = '8a216da870e2267e01714370cf4a33ea'
accToken = '3ad79c7cdc794addad5c4b82d3fad6d1'
appId = '8a216da870e2267e01714370cfaa33f1'

def send_message(phone, code, template_id):
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = phone
    datas = (code, '5')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)