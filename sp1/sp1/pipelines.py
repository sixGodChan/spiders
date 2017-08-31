# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import json


class Sp1Pipeline(object):
    def process_item(self, item, spider):
        return item


class JsonPipeline(object):
    def __init__(self):
        self.file = open('xiaohua.txt', 'w')

    def process_item(self, item, spider):
        v = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(v)
        self.file.write('\n')
        self.file.flush()
        return item


class FilePipeline(object):
    def __init__(self):
        if not os.path.exists('img'):
            os.makedirs('img')

    def process_item(self, item, spider):
        response = requests.get(item['url'], stream=True)
        file_name = '%s.%s' % (item['name'], item['type'])
        with open(os.path.join('img', file_name), mode='wb') as f:
            f.write(response.content)
        return item
