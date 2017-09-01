# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http.request import Request
import json
import urllib.parse


class JandanSpider(scrapy.Spider):
    '''
    图片点赞
    '''
    name = 'jandan'
    allowed_domains = ['jandan.net']
    # start_urls = ['http://jandan.net/']
    start_urls = ['http://jandan.net/ooxx/page-94#comments']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True, callback=self.parse)

    def parse(self, response):

        from scrapy.http.cookies import CookieJar

        # 获取cookies对象
        cookie_jar = CookieJar()  # cookie_jar，中封装了cookies
        cookie_jar.extract_cookies(response, response.request)  # 去response中获取cookies

        hxs = Selector(response).xpath('//ol[@class="commentlist"]/li')
        for item in hxs:
            v = item.xpath('.//div[@class="jandan-vote"]/span/a[@class="comment-like like"]/@data-id').extract()
            url = 'http://jandan.net/jandan-vote.php'
            data_id = int(v[0])

            body_dict = {
                'comment_id': data_id,
                'like_type': 'pos',
                'data_type': 'comment'
            }

            data = urllib.parse.urlencode(body_dict)
            yield Request(
                url=url,
                method='POST',
                headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                         'Host': 'jandan.net',
                         'Referer': 'http://jandan.net/ooxx',
                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                         'X-Requested-With': 'XMLHttpRequest'},
                cookies=cookie_jar,
                body=data,
                callback=self.parse2
            )

        page = Selector(response).xpath('//div[@class="comments"]/div[@class="cp-pagenavi"]/a[@href]/@href').extract()
        print(page[0])

        yield Request(url=page[0], dont_filter=True, callback=self.parse)

    def parse2(self, response):
        print(response.text)
        # pass
