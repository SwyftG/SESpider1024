# -*- coding: utf-8 -*-

# Scrapy settings for Email1024 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Email1024'

SPIDER_MODULES = ['Email1024.spiders']
NEWSPIDER_MODULE = 'Email1024.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Email1024 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 20

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Email1024.middlewares.Email1024SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Email1024.middlewares.Email1024DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Email1024.pipelines.Email1024Pipeline': 300,
   'Email1024.pipelines.Email1024FilePipeline': 1,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

SPIDER_NAME = "SE1024Spider"
ROOT_URL = "https://cc.cbcb.us/"        # 这里需要更新到最新的地址

FILES_STORE = 'teasure_src'         # 文件存储路径

MAX_PAGES = 10              # 可手动设置最大爬取单个区最大页面数，相配多大就配多大
BLOCK_INFO = {
    15: "亚洲有码",
    2: "亚洲无码",
    25: "国产原创",
    4: "欧美电影",
    26: "中字原创"
}

                                    # 这里是用126邮箱做例子，并不局限126邮箱
SMTP_HOST = "smtp.126.com"          # 发送邮件的smtp服务器
SMTP_USER = "XXXXXX@126.com"       # 用于登录smtp服务器的用户名，也就是发送者的邮箱
SMTP_PWD = "XXXXXXX"             # 授权码，和用户名user一起，用于登录smtp， 非邮箱密码
SMTP_PORT = 25                      # smtp服务器SSL端口号，默认是465，具体是什么，网上一搜邮箱域名和他的smtp就知道了
SMTP_SENDER = "XXXXXX@126.com"      # 发送方的邮箱
SMTP_TO_LIST = ["YYYYYY@126.com", "ZZZZZZ@126.com"]     # 发送目标邮箱地址，是个list

