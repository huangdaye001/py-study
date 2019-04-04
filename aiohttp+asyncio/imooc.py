import aiohttp
import asyncio
import pymongo
from fake_useragent import UserAgent
from lxml import etree

client=pymongo.MongoClient()
db=client['test']
collection=db['imoocClass']
ua=UserAgent()
sema=asyncio.Semaphore(5)
headers={ "User-Agent":ua.random }

def prase_content(content):
    tree=etree.HTML(content)
    lists=tree.xpath('//div[@class="course-card-container"]')
    '''<div class="course-card-container">
	<a target="_blank" href="/learn/1090" class="course-card">

		<div class="course-card-top">
			<img class="course-banner lazy" data-original="//img.mukewang.com/5c18cf540001ac8206000338-240-135.jpg" src="//img.mukewang.com/5c18cf540001ac8206000338-240-135.jpg" style="display: inline;">
						<div class="course-label">
												<label>Android</label>
											</div>
					</div>
		<div class="course-card-content">
			<h3 class="course-card-name">Flutter入门与案例实战</h3>
			<div class="clearfix course-card-bottom">
				<div class="course-card-info">
					<span>入门</span><span><i class="icon-set_sns"></i>10632</span>
				</div>
				<p class="course-card-desc">带你入门Flutter，并完成属于自己的第一个Flutter小案例。</p>
			</div>
		</div>
	</a>
    </div>'''
    for list in lists:
        data={
            'name':list.xpath('.//h3/text()')[0],
            'type':list.xpath('.//span[last()-1]/text()')[0],
            'number':list.xpath('.//span[last()]/text()')[0],
            'href':'https://www.imooc.com'+list.xpath('.//a/@href')[0],
            'desc':list.xpath('.//p[last()]/text()')[0],
        }
        collection.insert_one(data)
    print('添加数据成功！')
async def get_info(url):
    async with aiohttp.ClientSession(headers=headers) as Session:
        async with Session.get(url,timeout=3) as response:
            content=await response.text()
            print('正在爬取%s'%url)
            prase_content(content)

async def get(url):
    with await(sema):
        await get_info(url)

def main():
    url='https://www.imooc.com/course/list?page={}'
    urls=[url.format(page) for page in range(1,29)]#29
    loop=asyncio.get_event_loop()
    tasks=[get(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
if __name__ == '__main__':
    main()