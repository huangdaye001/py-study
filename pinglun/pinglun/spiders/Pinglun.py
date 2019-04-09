# -*- coding: utf-8 -*-
'''
爬取JD华为荣耀10评论
https://item.jd.com/7081550.html#comment
'''
import scrapy
from fake_useragent import UserAgent
import re
import json
from pinglun.items import PinglunItem
ua=UserAgent()
class PinglunSpider(scrapy.Spider):
    name = 'Pinglun'
    allowed_domains = ['sclub.jd.com']
    start_urls = ['https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv89694&productId=7081550&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(page)for page in range(0,10)]

    def parse(self, response):
        pattern=r'fetchJSON_comment98vv89694\((.*?)\);'
        data=re.findall(pattern,response.body_as_unicode(),re.S)
        content=json.loads(data[0])
        lists=content['comments']
        item=PinglunItem()
        for list in lists:
            item['nickname']=list['nickname']
            item['content'] = list['content']
            item['creationTime'] = list['creationTime']
            item['usefulVoteCount'] = list['usefulVoteCount']
            item['productColor'] = list['productColor']
            item['productSize'] = list['productSize']
            item['userClientShow'] = list['userClientShow']
            yield item

