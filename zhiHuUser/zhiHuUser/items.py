# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuuserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    用户名=scrapy.Field()
    职位=scrapy.Field()
    行业=scrapy.Field()
    教育经历=scrapy.Field()
    回答=scrapy.Field()
    提问=scrapy.Field()
    文章=scrapy.Field()
    专栏=scrapy.Field()
    想法=scrapy.Field()
    个人成就=scrapy.Field()
    关注了=scrapy.Field()
    关注者=scrapy.Field()


