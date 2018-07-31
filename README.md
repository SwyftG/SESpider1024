# SESpider1024

Scrapy 高阶玩法：

-  爬取1024社区
-  将种子和种子配图通过FilesPipeline快速下载到本地
-  将种子和种子配图可以通过Email发送到指定邮箱

酸爽



### 使用方法

在 settings.py 文件里面，只需要配置：

```py
ROOT_URL = "https://cc.cbcb.us/"        # 这里需要更新到最新的地址
									# 这里是用126邮箱做例子，并不局限126邮箱
SMTP_HOST = "smtp.126.com"          # 发送邮件的smtp服务器
SMTP_USER = "XXXXXX@126.com"       # 用于登录smtp服务器的用户名，也就是发送者的邮箱
SMTP_PWD = "XXXXXXX"             # 授权码，和用户名user一起，用于登录smtp， 非邮箱密码
SMTP_PORT = 25                      # smtp服务器SSL端口号，默认是465，具体是什么，网上一搜邮箱域名和他的smtp就知道了
SMTP_SENDER = "XXXXXX@126.com"      # 发送方的邮箱
SMTP_TO_LIST = ["YYYYYY@126.com", "ZZZZZZ@126.com"]     # 发送目标邮箱地址，是个list
```

同时需要注意，邮箱的配置，目前可以参考[这篇文章](https://www.cnblogs.com/xcblogs-python/p/5727238.html)设置即可，随后会更新文档。

## 大家慢慢爽

关注微信公众号『皮克啪的铲屎官』，天天硬核，惊喜不断。