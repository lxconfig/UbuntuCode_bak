

# 图片验证码的redis有效期 单位秒
IMAGE_CODE_REDIS_EXPIRES = 180

# 短信验证码的redis有效期 单位秒
SMS_CODE_REDIS_EXPIRES = 300

# 发送短信验证码的间隔时间 单位秒
SEND_SMS_CODE_INTERVAL = 60

# 尝试登陆的最大次数
LOGIN_ERROR_MAX_TIMES = 5

# 禁止登录的时间限制 单位秒
LOGIN_ERROR_FORBID_TIME = 600

# 七牛存储用户头像的url
QINIU_URL_DOMAIN = "http://q8eefndmq.bkt.clouddn.com/"

# redis中城区数据缓存的过期时间  单位秒
AREA_INFO_REDIS_CACHE_EXPIRES = 7200

# 首页房屋图片最大展示张数
INDEX_PAGE_IMAGE_MAX = 5

# 首页轮播房屋图片缓存时间
HOME_PAGE_REDIS_EXPIRES = 7200

# 房屋数据的缓存过期时间  单位秒
HOUSE_DETAIL_REDIS_EXPIRES = 7200

# 房屋详细信息中评论展示的最大条数
HOUSE_DETAIL_COMMENT_DISPLAY_COUNTS = 5

# 房屋列表页面中显示数据的条数
HOUSE_LIST_PAGE_CAPACITY = 2

# 房屋列表页面查询条件对应结果缓存时间 单位秒
HOUSE_LIST_PAGE_CACHE_EXPIRES = 7200