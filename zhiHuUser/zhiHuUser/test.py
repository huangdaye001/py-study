import requests
from lxml import etree
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'Accept-Encoding',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'Cookie':'_zap=45c1ae3f-8325-4ca5-a5dc-a7eb3af50b7a; d_c0="AMDlChN4PQ-PTjFNcM50jVP1wZIWWW5gQVU=|1554603155"; q_c1=00e69b7778a2421c90ba4ee5f4d1ae33|1554603159000|1554603159000; __gads=ID=0017a3b5dd9706de:T=1554603167:S=ALNI_MYY5RnG7AKNDqZi-ET8liFkZv1xrA; capsion_ticket="2|1:0|10:1554605551|14:capsion_ticket|44:OTUxYjNlNTQ0ODFmNDQyMDg0MmIwMGYxZGFkZmE5Y2M=|62a3a4f15ac87852b65ffd45d6d6ad0a1f0c783d27e45483eacd8d6f9bda1779"; z_c0="2|1:0|10:1554605576|4:z_c0|92:Mi4xSjQzUkF3QUFBQUFBd09VS0UzZzlEeVlBQUFCZ0FsVk5DTFNXWFFBNlhKaGtDMTVpQ2xLbjZXVy1rdWpLbl9VRmJ3|7bf817f85c026e1f7831e6318bcd40fa5d73c46df374e6e5641824c772065b5c"; tst=r; _xsrf=fd85b1d0-6fb5-40d6-96cd-65ad9980481b',
    'Host':'www.zhihu.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
}
if __name__ == '__main__':
    url='https://www.zhihu.com/people/chen-ke-55-65/following'
    content=requests.get(url,headers=DEFAULT_REQUEST_HEADERS).content.decode()
    tree=etree.HTML(content)
    username=tree.xpath('//h1[@class="ProfileHeader-title"]/span[1]/text()')[0]
    zhiwei=tree.xpath('//h1[@class="ProfileHeader-title"]/span[2]/text()')[0]
    hangye=tree.xpath('string(//div[@class="ProfileHeader-info"]/div[1])')
    jiaoyu=tree.xpath('string(//div[@class="ProfileHeader-info"]/div[2])')
    lists=tree.xpath('//ul[@class="Tabs ProfileMain-tabs"]//span[1]/text()')
    huida=lists[0]
    tiwen=lists[1]
    wenzhang=lists[2]
    zhuanlan=lists[3]
    xiangfa=lists[4]
    chengjiu=tree.xpath('string(//div[@class="Profile-sideColumnItems"]/div[1])')+','+tree.xpath('string(//div[@class="Profile-sideColumnItems"]/div[2])')+','+tree.xpath('string(//div[@class="Profile-sideColumnItems"]/div[3])')+','+tree.xpath('string(//div[@class="Profile-sideColumnItems"]/div[4])')

    guanzhu=tree.xpath('//strong[@class="NumberBoard-itemValue"]/text()')[0]
    guanzhuzhe=tree.xpath('//strong[@class="NumberBoard-itemValue"]/text()')[1]
    print(username)
    print(zhiwei)
    print(hangye)
    print(jiaoyu)
    print(huida)
    print(tiwen)
    print(wenzhang)
    print(zhuanlan)
    print(xiangfa)
    print(chengjiu.replace('\n','').replace(' ','').replace('1认证信息','认证信息:').replace('文章','文章,')
          )

    print(guanzhu)
    print(guanzhuzhe)
