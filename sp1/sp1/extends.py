from scrapy import signals


class MyExtension(object):
    def __init__(self):
        # self.value = value
        pass

    @classmethod
    def from_crawler(cls, crawler):
        # val = crawler.settings.getint('MMMM')
        # ext = cls(val)
        ext = cls()

        # 在scrapy中注册信号：指定在爬虫开始的时候，触发信号时执行spider_opened函数
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        # 在scrapy注册信号：指定在爬虫结束的时候，触发信号时执行spider_closed函数
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)

        return ext

    def spider_opened(self, spider):
        print('spider open, this is signals')

    def spider_closed(self, spider):
        print('close,signals')
