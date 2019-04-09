# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv


class StudyscrapyPipeline(object):
    def __init__(self):
        store_file=os.path.dirname(__file__)+'/spiders/school.csv'
        self.file=open(store_file,'a+',newline='',encoding='utf-8')
        self.writer=csv.writer(self.file)

    def process_item(self, item, spider):
        try:
            self.writer.writerow((
                item['uni_name'],
                item['uni_id'],
                item['city_code'],
                item['uni_type'],
                item['slogo'],
                item['rank'],
                item['safehard']
            ))
        except Exception as e:
            print(e)
    def close_spider(self,spider):
        self.file.close()