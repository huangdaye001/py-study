# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from zhiHuUser.items import ZhihuuserItem
class ZhihuuserSpider(scrapy.Spider):
    name = 'zhihuUser'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/people/chen-ke-55-65/following']

    def parse(self, response):
        content=response.body_as_unicode()
        tree=etree.HTML(content)
        item=ZhihuuserItem()
        item['用户名'] =tree.xpath('//h1[@class="ProfileHeader-title"]/span[1]/text()')[0]
        if tree.xpath('//h1[@class="ProfileHeader-title"]/span[2]/text()'):
            item['职位'] =tree.xpath('//h1[@class="ProfileHeader-title"]/span[2]/text()')[0]
        else:
            item['职位'] =''
        item['行业'] =tree.xpath('string(//div[@class="ProfileHeader-info"]/div[1])')
        item['教育经历'] =tree.xpath('string(//div[@class="ProfileHeader-info"]/div[2])')
        item['回答'] =tree.xpath('//ul[@class="Tabs ProfileMain-tabs"]//span[1]/text()')[0]
        item['提问'] =tree.xpath('//ul[@class="Tabs ProfileMain-tabs"]//span[1]/text()')[1]
        item['文章'] =tree.xpath('//ul[@class="Tabs ProfileMain-tabs"]//span[1]/text()')[2]
        item['专栏'] =tree.xpath('//ul[@class="Tabs ProfileMain-tabs"]//span[1]/text()')[3]
        item['想法'] =tree.xpath('//ul[@class="Tabs ProfileMain-tabs"]//span[1]/text()')[4]
        item['个人成就'] =tree.xpath('string(//div[@class="Profile-sideColumnItems"]/div[1])')+','+tree.xpath('string(//div[@class="Profile-sideColumnItems"]/div[2])')+','+tree.xpath('string(//div[@class="Profile-sideColumnItems"]/div[3])')+','+tree.xpath('string(//div[@class="Profile-sideColumnItems"]/div[4])').replace('\n','').replace(' ','').replace('1认证信息','认证信息:').replace('文章','文章,')
        if tree.xpath('//strong[@class="NumberBoard-itemValue"]/text()'):
            item['关注了'] = tree.xpath('//strong[@class="NumberBoard-itemValue"]/text()')[0]
            item['关注者'] = tree.xpath('//strong[@class="NumberBoard-itemValue"]/text()')[1]
        else:
            item['关注了'] =0
            item['关注者'] =0
        yield item
        lists=tree.xpath('//a[@class="UserLink-link"]/@href')
        for list in lists:
            url='https:'+list+'/following'
            yield scrapy.Request(url,callback=self.parse)
