'''
爬取51cto课程信息
radis存储
'''
import aiohttp
import asyncio
from lxml import etree
from fake_useragent import UserAgent
import redis
import json

pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)



ua=UserAgent()
headers={
    'User-Agent':ua.random,
}
def prase_content(content):
    tree=etree.HTML(content)
    lists=tree.xpath('//div[@class="cList_Item"]')
    print(lists)
    for list in lists:
        price=list.xpath('.//div[@class="price"]/h4[1]/text()')
        if price:
            number=price[0]
        else:
            number='会员限免'
        data={
            'title':list.xpath('.//a[@class="save-click"]/@title')[0],
            'href': list.xpath('.//a[@class="save-click"]/@href')[0],
            'class': list.xpath('.//div[@class="course_infos"]/p[1]/text()')[0],
            'number': list.xpath('.//p[@class="fr study_nums"]/text()')[0],
            'val': list.xpath('.//div[@class="stars02"]/@val')[0],
            'des': list.xpath('.//div[@class="course_target"]/text()')[0].replace('\n','').replace('    ',''),
            'price':number,
        }
        r.sadd('51cto',json.dumps(data))
    print('添加数据成功')
async def get_info(url):
    async with aiohttp.ClientSession(headers=headers) as Session:
        try:
            async with Session.get(url,timeout=5) as response:
                content=await response.text()
                print('正在爬取%s'%url)
                prase_content(content)
        except Exception as e:
            print(e)
sema=asyncio.Semaphore(5)
async def get(url):
    with await(sema):
        await get_info(url)

def main():
    url='https://edu.51cto.com/courselist/index-p{}.html?edunav='
    urls=[url.format(page) for page in range(1,3)]
    loop=asyncio.get_event_loop()
    tasks=[get(url)for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    for i in r.sscan_iter("51cto"):
        print(json.loads(i))

if __name__ == '__main__':
    main()