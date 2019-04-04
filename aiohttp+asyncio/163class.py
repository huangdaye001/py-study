''''
获取网易云课堂  人工智能分类（480000003127010）课程信息  别的课程更改post frontCategoryId即可
是用aiohttp+asyncio
pymongo存储
'''
import aiohttp
import asyncio
from fake_useragent import UserAgent
import pymongo
import json

client=pymongo.MongoClient()
db=client['test']
collection=db['163study']

ua=UserAgent()
headers = {"Accept":"application/json", "Host":"study.163.com", "Origin":"https://study.163.com", "Content-Type":"application/json", "Referer":"https://study.163.com/courses", "User-Agent":ua.random }
url = 'https://study.163.com/p/search/studycourse.json'
sema=asyncio.Semaphore(2)
post_lists=[]
async def get(postdata):
    async with aiohttp.ClientSession() as Session:
        try:
            async with Session.post(url,headers=headers,data=json.dumps(postdata),timeout=3) as rp:
                data=await rp.text()
                jsondata=json.loads(data)
                lists = jsondata['result']['list']
                if lists:
                    for list in lists:
                        data={
                            'productName':list['productName'],
                            'description': list['description'],
                            'score': list['score'],
                            'imgUrl': list['imgUrl'],
                            'originalPrice': list['originalPrice'],
                            'discountPrice': list['discountPrice'],
                        }
                        collection.insert_one(data)
                    print('添加数据成功')
        except Exception as e:
            print(e)
            print('获取数据失败')


async def get_html(postdata):
    with await(sema):
        await get(postdata)


def main():
    #post  构建参数
    for page in range(1,10):
        postdata = {
            'activityId': 0,
            'frontCategoryId': 480000003127010,
            'keyword': '',
            'orderType': 50,
            'pageIndex': page,
            'pageSize': 50,
            'priceType': - 1,
            'relativeOffset': 100,
            'searchTimeType': - 1,
        }
        post_lists.append(postdata)
    loop=asyncio.get_event_loop()
    tasks=[get_html(postdata) for postdata in post_lists]
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()