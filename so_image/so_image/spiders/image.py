# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    # BASE_URL = 'http://image.so.com/zj?ch=art&sn=30&listtype=new&t
    start_index = 0

    def parse(self, response):
        # 使用json 模块解析响应结果
        infos = json.loads(response.body.decode('utf-8'))
        # 提取所有图片下载url 到一个列表， 赋给item的'image_urls'字段
        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}
        # 如count 字段大于0，并且下载数量不足MAX_DOWNLOAD_NUM，继续获取下一页图片信息
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield Request(self.BASE_URL % self.start_index)
