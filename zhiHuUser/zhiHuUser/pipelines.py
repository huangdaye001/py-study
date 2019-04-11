# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import pickle
pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)

class ZhihuuserPipeline(object):
    def process_item(self, item, spider):
        r.sadd('zhiHuUser3', pickle.dumps(item))
        print('添加数据成功')