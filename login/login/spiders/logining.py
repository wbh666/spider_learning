# -*- coding: utf-8 -*-
import scrapy
from ..items import LoginFormItem


class LoginingSpider(scrapy.Spider):
    name = 'logining'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    def parse(self, response):
        sel = response.xpath('//div[@style]/input')
        print(sel.extract())
        # fd = dict(zip(sel.xpath('./@name').extract(), sel.xpath('./@val').extract(), sel.xpath('./@next').extract()))
