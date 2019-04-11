# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

cilent=pymongo.MongoClient('127.0.0.1',27017)
db=cilent['test']
collection=db['jueJin']
class JuejinPipeline(object):

    def process_item(self, item, spider):
        try:
            collection.insert_one(item)
            print('插入数据成功')
        except Exception as e:
            print(e)