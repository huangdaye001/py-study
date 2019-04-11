import requests
from lxml import etree

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Cookie': 'td_cookie=18446744069430823882; QINGCLOUDELB=76207815f7e5b4254ee78b6e114322bbab7e48fb3972913efd95d72fe838c4fb|XK2Rc|XK2RX; ab={}; Hm_lvt_93bbd335a208870aa1f296bcd6842e5e=1554878678; Hm_lpvt_93bbd335a208870aa1f296bcd6842e5e=1554878831; gr_user_id=8fac767f-243d-4078-ba3b-580f48cf323c; gr_session_id_89669d96c88aefbc=a34c9ed8-8770-4c9a-9dd5-6cdb5a16e32b; gr_session_id_89669d96c88aefbc_a34c9ed8-8770-4c9a-9dd5-6cdb5a16e32b=true; _ga=GA1.2.1209351910.1554878679; _gid=GA1.2.360261370.1554878679',
    'Host': 'juejin.im',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
}
if __name__ == '__main__':
    url="https://juejin.im/user/58b7d0c4570c35006c477419/following"
    content=requests.get(url,headers=DEFAULT_REQUEST_HEADERS).content
    tree=etree.HTML(content.decode())
    username = tree.xpath('//h1[@class="username"]/text()')[0]
    jobTitle = tree.xpath('string(//span[@class="content"])')
    miss=tree.xpath('string(//div[@class="intro"])')
    zhuanlan = tree.xpath('//a[@class="nav-item"][2]/div[@class="item-count"]/text()')[0]
    feidian = tree.xpath('//a[@class="nav-item"][3]/div[@class="item-count"]/text()')[0]
    fenxiang = tree.xpath('//a[@class="nav-item"][4]/div[@class="item-count"]/text()')[0]
    xiaocezi = tree.xpath('//a[@class="nav-item"][5]/div[@class="item-count"]/text()')[0]
    zan = tree.xpath('//div[@class="nav-item not-in-scroll-mode"]/div[@class="item-count"]/text()')[0]
    beidianzanshu=tree.xpath('string(//div[@class="block-body"]/div[1])')
    beiread=tree.xpath('string(//div[@class="block-body"]/div[2])')
    guanzhu=tree.xpath('//div[@class="follow-block block shadow"]/a[1]/div[2]/text()')[0]
    beiguanzhu=tree.xpath('//div[@class="follow-block block shadow"]/a[2]/div[2]/text()')[0]
    join_time=tree.xpath('//time[@class="time"]/text()')[0]
    print(username)
    print(jobTitle)
    print(miss)
    print(zhuanlan)
    print(feidian)
    print(fenxiang)
    print(xiaocezi)
    print(zan)
    print(beidianzanshu)
    print(beiread)
    print(guanzhu)
    print(beiguanzhu)
    print(join_time)