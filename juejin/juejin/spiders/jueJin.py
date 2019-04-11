# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from juejin.items import JuejinItem
class JuejinSpider(scrapy.Spider):
    name = 'jueJin'
    allowed_domains = ['juejin.im']
    start_urls = ['https://juejin.im/user/58b7d0c4570c35006c477419/following']

    def parse(self, response):
        content=response.body_as_unicode()
        tree=etree.HTML(content)
        item=JuejinItem()
        item['用户名']=tree.xpath('//h1[@class="username"]/text()')[0]
        item['工作标签']=tree.xpath('string(//span[@class="content"])')
        item['个性签名']=tree.xpath('string(//div[@class="intro"])')
        item['专栏']=tree.xpath('//a[@class="nav-item"][2]/div[@class="item-count"]/text()')[0]
        if tree.xpath('//a[@class="nav-item"][3]/div[@class="item-count"]/text()'):
            item['沸点']=tree.xpath('//a[@class="nav-item"][3]/div[@class="item-count"]/text()')[0]
        else:
            item['沸点'] =''
        item['分享']=tree.xpath('//a[@class="nav-item"][4]/div[@class="item-count"]/text()')[0]
        item['赞']=tree.xpath('//div[@class="nav-item not-in-scroll-mode"]/div[@class="item-count"]/text()')[0]
        item['小册子']=tree.xpath('//a[@class="nav-item"][5]/div[@class="item-count"]/text()')[0]
        item['个人成就']=tree.xpath('string(//div[@class="block-body"]/div[1])')+tree.xpath('string(//div[@class="block-body"]/div[2])')
        item['关注了']=tree.xpath('//div[@class="follow-block block shadow"]/a[1]/div[2]/text()')[0]
        item['关注者']=tree.xpath('//div[@class="follow-block block shadow"]/a[2]/div[2]/text()')[0]
        item['加入时间']=tree.xpath('//time[@class="time"]/text()')[0]
        yield item
        lists=tree.xpath('//a[@class="link"]/@href')
        for list in lists:
            url='https://juejin.im'+list+'/following'
            print(url)
            yield scrapy.Request(url,callback=self.parse)