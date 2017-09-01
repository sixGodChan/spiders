# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request


class JandanSpider(scrapy.Spider):
    name = 'jandan'
    # allowed_domains = ['dig.chouti.com']
    # start_urls = ['http://dig.chouti.com/']
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        # pass

        from scrapy.http.cookies import CookieJar

        # 获取cookies对象
        cookie_jar = CookieJar()  # cookie_jar，中封装了cookies
        cookie_jar.extract_cookies(response, response.request)  # 去response中获取cookies

        # 获取cookies字典
        self.cookie_dict = {}

        for k, v in cookie_jar._cookies.items():
            for i, j in v.items():
                for m, n in j.items():
                    self.cookie_dict[m] = n.value

        yield Request(url='http://jandan.net/ooxx', callback=self.parse, dont_filter=False, cookies=cookie_jar)
