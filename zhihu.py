'''
获取知乎某问题所有答案里的所有图片（gif除外）
'''
import requests
from fake_useragent import UserAgent
import json
import re
import aiohttp
import asyncio
import os
ua=UserAgent()
headers={
    'Cookie':'_zap=45c1ae3f-8325-4ca5-a5dc-a7eb3af50b7a; d_c0="AMDlChN4PQ-PTjFNcM50jVP1wZIWWW5gQVU=|1554603155"; q_c1=00e69b7778a2421c90ba4ee5f4d1ae33|1554603159000|1554603159000; __gads=ID=0017a3b5dd9706de:T=1554603167:S=ALNI_MYY5RnG7AKNDqZi-ET8liFkZv1xrA; _xsrf=dc3a96f2-5412-44e0-ba48-e4d95a11de7b; capsion_ticket="2|1:0|10:1554605551|14:capsion_ticket|44:OTUxYjNlNTQ0ODFmNDQyMDg0MmIwMGYxZGFkZmE5Y2M=|62a3a4f15ac87852b65ffd45d6d6ad0a1f0c783d27e45483eacd8d6f9bda1779"; z_c0="2|1:0|10:1554605576|4:z_c0|92:Mi4xSjQzUkF3QUFBQUFBd09VS0UzZzlEeVlBQUFCZ0FsVk5DTFNXWFFBNlhKaGtDMTVpQ2xLbjZXVy1rdWpLbl9VRmJ3|7bf817f85c026e1f7831e6318bcd40fa5d73c46df374e6e5641824c772065b5c"; tst=r',
    'User-Agent':ua.random,
    'Host':'www.zhihu.com',
}
he={

}
url_format = "https://www.zhihu.com/api/v4/questions/{}/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&offset={}&limit=20&sort_by=default&platform=desktop"
async def get_content(url):
    async with aiohttp.ClientSession() as Session:
        try:
            print('爬取%s'%url)
            async with Session.get(url,headers=headers,timeout=5) as response:
                content=await response.text()
                jsondata = json.loads(content)
                lists=jsondata['data']
                pattern = r'data-actualsrc="(.*?.jpg)"/>'
                for list in lists:
                    imgs = re.findall(pattern, list['content'], re.S)
                    for img in imgs:
                        print(img)
                        headers1={
                            'User-Agent':ua.random,
                            'Cookie':'_zap=37382180-fd02-45e3-b309-95f9c6f6a4dd',
                        }
                        async with Session.get(img,headers=headers1,timeout=5) as response:
                            print('下载%s'%img)
                            imgdata = await response.read()
                            filename = img.split('/')[-1]
                            filepath = 'imgs/' + filename
                            with open(filepath, 'wb') as fp:
                                fp.write(imgdata)
        except Exception as e:
            print(e)
            print('获取数据失败')

sema=asyncio.Semaphore(10)
async def get(url):
    with await(sema):
        await get_content(url)

def main():
    id=input('请输入你要查找问题的id：')
    #获取回答数  切割url   limit=20 setoff=num  每次20个答案从num开始
    url=url_format.format(id,0)
    content=requests.get(url,headers=headers,timeout=8).text
    jsondata=json.loads(content)
    number=jsondata['paging']['totals']//20+1
    #创建文件夹存储图片
    if not os.path.exists('imgs'):
        os.mkdir('imgs')
    print(number)
    loop=asyncio.get_event_loop()
    urls=[(url_format.format(id,20*num))for num in range(0,number)]
    tasks=[get(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()