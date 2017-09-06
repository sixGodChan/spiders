# -*- coding: utf-8 -*-
import scrapy


class JandanSpider(scrapy.Spider):
    name = 'jandan'
    allowed_domains = ['jandan.com']
    start_urls = ['http://jandan.net/']

    def parse(self, response):
        print(response)
