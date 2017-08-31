# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import requests
from scrapy.http.request import Request

import os
import json


class JandanImgSpider(scrapy.Spider):
    name = 'jandan_img'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx/page-1#comments/']

    def parse(self, response):
        hxs = Selector(response).xpath('//ol[@class="commentlist"]')
        for item in hxs:
            v = item.xpath('./li/@id').extract()
            v2 = item.xpath('./li/div/div/div[@class="text"]/p/img/@src').extract()
            for i, u in enumerate(v2):
                url = 'http:%s' % u
                type = u.split('.')[-1]
                name = v[i]
                print(url, name, type)
                from ..items import JandanImgItem
                obj = JandanImgItem(name=name, type=type, url=url)
                yield obj

        page = Selector(response).xpath('//div[@class="comments"]/div[@class="cp-pagenavi"]/a[@href]/@href').extract()
        page = [page[0]]
        print(page)
        # 规则
        for url in page:
            yield Request(url=url, callback=self.parse)
