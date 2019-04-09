# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv

class HuxiuPipeline(object):
    def __init__(self):
        store_file=os.path.dirname(__file__)+'/spiders/huxiu.csv'
        self.file=open(store_file,'a+',newline='',encoding='utf8')
        self.writer=csv.writer(self.file)
    def process_item(self, item, spider):
        self.writer.writerow((
            item['title'],
            item['summary'],
            item['share_url'],
            item['username'],
            item['time'],
            item['agree'],
        ))
        print(item)
        print('写入数据成功！')
    def colse_spider(self,spider):
        self.file.close()