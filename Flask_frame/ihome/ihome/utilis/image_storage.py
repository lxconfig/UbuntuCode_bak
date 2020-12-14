from qiniu import Auth, put_data, etag, urlsafe_base64_encode
import qiniu.config


#需要填写你的 Access Key 和 Secret Key
access_key = 'IfBIvWJ0t2wMrtLFaM3ougu9JZQnYrwinUUmJqpF'
secret_key = 'o6-grZVIprf6CB-hXRhpw9ipdLn93GaokvhJYMH1'


def storage(file_data):
    """将图片存储到七牛"""

    #构建鉴权对象
    q = Auth(access_key, secret_key)

    #要上传的空间
    bucket_name = 'iho'

    #上传后保存的文件名
    # key = 'my-python-logo.png'

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    #要上传文件的本地路径
    # localfile = './sync/bbb.jpg'

    ret, info = put_data(token, None, file_data)

    # print(ret)
    # print("*" * 10)
    # print(type(info))
    # print(info)
    # print(info.status_code)

    if info.status_code == 200:
        # 上传成功，返回文件名
        return ret.get("key")
    else:
        # 上传失败，抛出异常
        raise Exception("上传qiniu失败")

if __name__ == "__main__":
    with open("./1.png", "rb") as f:
        file_data = f.read()
        storage(file_data)