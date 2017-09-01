# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import json

from scrapy.exceptions import DropItem


class JsonPipeline(object):
    def __init__(self):
        self.file = None

    def process_item(self, item, spider):
        """
        :param item: 爬虫中yield回来的对象
        :param spider: 爬虫对象,JandanImgSpider()类的对象
        :return: 
        """
        v = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(v)
        self.file.write('\n')
        self.file.flush()
        # return表示会被后续的pipeline继续处理
        return item

        # 表示将item丢弃，不会被后续pipeline处理
        # raise DropItem()

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        # val = crawler.settings.get('MMMM')  # 从配置文件获取链接数据库数据
        print('执行pipeline的from_crawler，进行实例化对象')
        return cls()

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('打开爬虫')
        self.file = open('jandan.txt', 'a+')

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        self.file.close()
        print('关闭爬虫')


# class JsonPipeline(object):
#     def __init__(self):
#         self.file = open('jandan.txt', 'w')
#
#     def process_item(self, item, spider):
#         v = json.dumps(dict(item), ensure_ascii=False)
#         self.file.write(v)
#         self.file.write('\n')
#         self.file.flush()
#         return item


class FilePipeline(object):
    def __init__(self):
        if not os.path.exists('img'):
            os.makedirs('img')

    def process_item(self, item, spider):
        response = requests.get(item['url'], headers={'Host': 'wx1.sinaimg.cn'}, stream=True)
        file_name = '%s' % (item['name'])
        with open(os.path.join('img', file_name), mode='wb') as f:
            f.write(response.content)
        return item
