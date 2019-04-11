# -*- coding: utf-8 -*-

# Scrapy settings for zhiHuUser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhiHuUser'

SPIDER_MODULES = ['zhiHuUser.spiders']
NEWSPIDER_MODULE = 'zhiHuUser.spiders'
ITEM_PIPELINES={
    'zhiHuUser.pipelines.ZhihuuserPipeline':300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhiHuUser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'Accept-Encoding',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'Cookie':'_zap=45c1ae3f-8325-4ca5-a5dc-a7eb3af50b7a; d_c0="AMDlChN4PQ-PTjFNcM50jVP1wZIWWW5gQVU=|1554603155"; q_c1=00e69b7778a2421c90ba4ee5f4d1ae33|1554603159000|1554603159000; __gads=ID=0017a3b5dd9706de:T=1554603167:S=ALNI_MYY5RnG7AKNDqZi-ET8liFkZv1xrA; capsion_ticket="2|1:0|10:1554605551|14:capsion_ticket|44:OTUxYjNlNTQ0ODFmNDQyMDg0MmIwMGYxZGFkZmE5Y2M=|62a3a4f15ac87852b65ffd45d6d6ad0a1f0c783d27e45483eacd8d6f9bda1779"; z_c0="2|1:0|10:1554605576|4:z_c0|92:Mi4xSjQzUkF3QUFBQUFBd09VS0UzZzlEeVlBQUFCZ0FsVk5DTFNXWFFBNlhKaGtDMTVpQ2xLbjZXVy1rdWpLbl9VRmJ3|7bf817f85c026e1f7831e6318bcd40fa5d73c46df374e6e5641824c772065b5c"; tst=r; _xsrf=fd85b1d0-6fb5-40d6-96cd-65ad9980481b',
    'Host':'www.zhihu.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhiHuUser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhiHuUser.middlewares.ZhihuuserDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhiHuUser.pipelines.ZhihuuserPipeline': 300,
#}

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
