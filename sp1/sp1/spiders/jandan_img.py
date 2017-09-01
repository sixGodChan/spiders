# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http.request import Request
from scrapy.http.cookies import CookieJar


class JandanImgSpider(scrapy.Spider):
    name = 'jandan_img'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx/page-300#comments/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True, headers={'Host': 'jandan.net'}, callback=self.parse)

    def parse(self, response):
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)

        hxs = Selector(response).xpath('//ol[@class="commentlist"]')
        for item in hxs:
            v2 = item.xpath('./li/div/div/div[@class="text"]/p/img/@src').extract()
            for u in v2:
                url = 'http:%s' % u
                name = u.split('/')[-1]
                print(url)
                from ..items import JandanImgItem
                yield JandanImgItem(name=name, url=url)

        page = Selector(response).xpath('//div[@class="comments"]/div[@class="cp-pagenavi"]/a[@href]/@href').extract()
        print(page[0])

        yield Request(url=page[0], dont_filter=True, headers={'Host': 'jandan.net'}, callback=self.parse)
