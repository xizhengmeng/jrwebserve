# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
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
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tutorial.pipelines.TutorialPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# DEFAULT_REQUEST_HEADERS = {
#   "Host": "itunes.apple.com",
#   "X-Apple-Tz": "28800",
#   "Connection": "keep-alive",
#   "Accept": "*/*",
#   "X-Apple-Store-Front": "143465-19,32",
#   "Proxy-Connection": "keep-alive",
#   "If-Modified-Since": "Mon, 30 Oct 2017 05:09:14 GMT",
#   "Accept-Language": "zh-Hans;q=1.0, en;q=0.9",
#   "Accept-Encoding": "gzip, deflate",
#   "X-Apple-I-MD-RINFO": "17106176",
#   "X-Apple-I-MD-M": "4yta1gxLU2/1yorU7oVB982KDbxQfTgDNV0Kx6rMh83dcH6GSFvvMX4j2xTK1pydINZyrdPRmrAqnMrx",
#   "User-Agent": "iTunes/12.5.5 (Macintosh; OS X 10.11.6) AppleWebKit/601.7.7",
#   "X-Apple-I-Client-Time": "2017-10-30T06:38:41Z",
#   "Referer": "https://itunes.apple.com/cn/app/%E4%BA%AC%E4%B8%9C%E9%87%91%E8%9E%8D-%E6%96%B0%E4%BA%BA%E9%A2%86666%E5%85%83%E5%A4%A7%E7%A4%BC%E5%8C%85/id895682747?mt=8",
#   "X-Apple-I-MD": "AAAABQAAABB/8E70ajsA2bpSsQneRzRzAAAAAQ==",
#   "X-Dsid": "1851386458",
#   "Cookie": "groupingPillToken=1_iphone; mt-asn-1851386458=5; mt-asn-1952598692=5; mt-tkn-1851386458=AquPBN7pBVJrtDMwCG1MrwviP60xe4f/EE45hsAOovLfR/ovUuHxcsKrlj2pxor0U9F3HIkuroemH+0MuFQnpjqUFC4oYoymULT5CpIKnJ3VpDni/Y/moZel5PjbSHG4GD+Ijl5r7uyk/NbjAbcP2c6m643pr8/RJ8pEGPfTmpVhsZJWGga7Uku1jMcsYZwUcq4thww=; mt-tkn-1952598692=AmPsxyX+Zm3hcSBdOCr1LAg942a/+QI1OZsorJ+0WD2wkyUHZ6Dv3jDaRipaZfgo7xzHgpeVUdtG70RFfh0FA5pOHGZGJ/5b/MiFc4VGex0OtgQ9XasD8i89/gI1Ai21Fi7kJkngVal3DewE6NPKYC8difiYN7R7wY/nH/Z3bcgGM9wio22SK/ZdDyrs38XhS717EKw=; X-Dsid=1851386458; itspod=24; mz_at0-1851386458=AwQAAAEBAAHWuQAAAABZo5zH8UZyjuA18kRtUGbvu8lLlA89jpk=; mz_at0-1952598692=AwQAAAEBAAHWUwAAAABX91VVP4AXK30/tKDBEUr2V9fwfUERl9A=; mz_at_ssl-1851386458=AwUAAAEBAAHWUwAAAABYFwZni0EdGJhw1mXiPHOZnkeCs8m3DaU=; mz_at_ssl-1952598692=AwUAAAEBAAHWUQAAAABXfIMB4QjT3cNSHm+BuLBHSWqkz1Ndd0g=; s_vi=[CS]v1|2B45BA5205011739-600001038013C541[CE]; xp_ab=1#isj11bm+3579+17Eg4xa0; xp_abc=17Eg4xa0; xp_ci=3z34ZpILzCUZz4Vrz9pTzlq8yrxrJ",
#   "iCloud-DSID": "1851386458"
# }

MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "Spider"  # 库名
MONGO_COLL = "Comment"  # collection名
# MONGO_USER = "zhangsan"
# MONGO_PSW = "123456"
