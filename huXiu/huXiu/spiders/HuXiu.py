# -*- coding: utf-8 -*-
import scrapy
import json
import time
from huXiu.items import HuxiuItem
class HuxiuSpider(scrapy.Spider):
    name = 'HuXiu'
    allowed_domains = ['www-api.huxiu.com']
    start_urls = ['https://www-api.huxiu.com/v1/article/list?recommend_time=']

    def parse(self, response):
        content=json.loads(response.body_as_unicode())
        last_dateline=content['data']['last_dateline']
        is_have_next_page=content['data']['is_have_next_page']
        lists=content['data']['dataList']
        print(last_dateline)
        print(is_have_next_page)

        item=HuxiuItem()
        try:
            for list in lists:
                item['title']=list['title']+'-'
                item['time'] = time.strftime("%Y--%m--%d %H:%M:%S-", time.localtime(int(list['dateline'])))
                item['share_url'] = list['share_url']+'-'
                item['summary'] = list['summary']+'-'
                item['username'] = list['user_info']['username']+'-'
                item['agree'] = list['count_info']['agree']+'-'
                yield item
        finally:
            if is_have_next_page:
                time.sleep(1)
                yield scrapy.Request('https://www-api.huxiu.com/v1/article/list?recommend_time={}'.format(last_dateline),callback=self.parse)
            else:
                print('爬取结束！')


