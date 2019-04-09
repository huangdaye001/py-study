# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PinglunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''用户名 评论 评论时间 点赞数 颜色 类型 客户端类型'''
    nickname=scrapy.Field()
    content=scrapy.Field()
    creationTime=scrapy.Field()
    usefulVoteCount=scrapy.Field()
    productColor=scrapy.Field()
    productSize=scrapy.Field()
    userClientShow=scrapy.Field()