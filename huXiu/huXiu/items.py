# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuxiuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    time=scrapy.Field()
    share_url = scrapy.Field()
    username = scrapy.Field()
    summary = scrapy.Field()
    agree = scrapy.Field()

