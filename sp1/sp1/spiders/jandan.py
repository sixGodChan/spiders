# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import requests
from scrapy.http.request import Request


class JandanSpider(scrapy.Spider):
    name = 'jandan'
    allowed_domains = ['jandan.net']
    # start_urls = ['http://jandan.net/']
    start_urls = ['http://jandan.net/ooxx/page-1#comments']

    def parse(self, response):
        hxs = Selector(response).xpath('//ol[@class="commentlist"]/li')
        for item in hxs:
            v = item.xpath('.//div[@class="jandan-vote"]/span/a[@class="comment-like like"]/@data-id').extract()
            url = 'http://jandan.net/jandan-vote.php'
            data_id = int(v[0])
            print(data_id)
            coo = '__cfduid=dde78912d201345a50d7a854acad0d0ac1503640019; voted_comment_3549225=1; voted_comment_3549451=1; voted_comment_3549450=1; voted_comment_3549449=-1; voted_comment_3549511=1; _ga=GA1.2.717260484.1503640017; _gid=GA1.2.1047465622.1504159931; voted_comment_3549510=1; voted_comment_3549509=1'
            res = requests.post(
                url=url,
                json={
                    'comment_id': data_id,
                    'like_type': 'pos',
                    'data_type': 'comment'
                },
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Cookie': coo,
                    'Host': 'jandan.net',
                    'Referer': 'http://jandan.net/ooxx',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            )
            res.encoding = 'utf8'
            print(res.text)

        page = Selector(response).xpath('//div[@class="comments"]/div[@class="cp-pagenavi"]/a[@href]/@href').extract()
        print(page)
        'http://jandan.net/ooxx/page-297#comments'


        # 规则
        for url in page:
            yield Request(url=url, callback=self.parse)