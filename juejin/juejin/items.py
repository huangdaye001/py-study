# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JuejinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    用户名 = scrapy.Field()
    工作标签 = scrapy.Field()
    个性签名=scrapy.Field()
    专栏 = scrapy.Field()
    沸点 = scrapy.Field()
    分享 = scrapy.Field()
    赞 = scrapy.Field()
    小册子 = scrapy.Field()
    个人成就 = scrapy.Field()
    关注了 = scrapy.Field()
    关注者 = scrapy.Field()
    加入时间 = scrapy.Field()

