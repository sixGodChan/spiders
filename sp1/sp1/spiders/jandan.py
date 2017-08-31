# -*- coding: utf-8 -*-
import scrapy


class JandanSpider(scrapy.Spider):
    name = 'jandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/']

    def parse(self, response):
        #pass
        print(response.text)
