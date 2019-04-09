# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv

class PinglunPipeline(object):
    def __init__(self):
        store_file=os.path.dirname(__file__)+'/spiders/JDpinglun.csv'
        self.file=open(store_file,'a+',newline='',encoding='utf-8')
        self.writer=csv.writer(self.file)
    def process_item(self, item, spider):
        try:
            self.writer.writerow((
                item['nickname'],
                item['content'],
                item['creationTime'],
                item['usefulVoteCount'],
                item['productColor'],
                item['productSize'],
                item['userClientShow'],
            ))
            print('数据存储完毕')
        except Exception as e:
            print(e)
    def close_spider(self,spider):
        self.file.close()