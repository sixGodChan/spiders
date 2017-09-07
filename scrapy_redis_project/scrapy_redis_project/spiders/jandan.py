# -*- coding: utf-8 -*-
# import scrapy
#
#
# class JandanSpider(scrapy.Spider):
#     name = 'jandan'
#     allowed_domains = ['jandan.com']
#     start_urls = ['http://jandan.net/']
#
#     def parse(self, response):
#         print(response)

# 起始URL从redis的Key中获取

from scrapy_redis.spiders import RedisSpider


class JandanSpider(RedisSpider):
    name = 'jandan'
    allowed_domains = ['jandan.com']
    start_urls = ['http://jandan.net/']  # 不用自己写url，自动去redis中拿

    def parse(self, response):
        print(response)

