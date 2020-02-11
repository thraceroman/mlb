# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from mlb.items import MlbItem


class VolmoeSpider(scrapy.Spider):
    name = 'volmoe'
    allowed_domains = ['volmoe.com']
    start_urls = ['https://volmoe.com/list/all,all,all,sortpoint,all,all/1.htm']

    def parse(self, response):
        item = MlbItem() 
        item["title"] = response.xpath("//tr[@class='listbg']//a/text()").extract()
        # 这个text()的第零项,是空????从1开始的?
        author = response.xpath("//tr[@class='listbg']/td/text()[5]").extract()
        item["author"] = list(map(lambda str:str[2:-2],author))
        item["num"] = response.xpath("//tr[@class='listbg']//font[@class='pagefoot']/text()").extract()
        # print(item["title"])
        # print(item["author"])
        # print(item["num"])
        yield item
        # 连爬5页
        # for i in range(2,6):
        #     url = "https://volmoe.com/list/all,all,all,sortpoint,all,all/"+str(i)+".htm"
        #     yield Request(url,callback=self.parse)
