'''
爬取京东商城  python图书 商品信息
selenium+Firefox
xpath解析 mongodb存储
'''
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import pymongo
client=pymongo.MongoClient()
db=client['test']
collection=db['jdpython']
option=Options()
option.add_argument('-headless')
driver=Firefox(firefox_options=option)
wait=WebDriverWait(driver,10)
Index=0
def get_info():
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,'//ul[@class="gl-warp clearfix"]')))
        print('正在爬取%s'%driver.current_url)
        tree=etree.HTML(driver.page_source)
        lists=tree.xpath('//li[@class="gl-item"]')
        for li in lists:
            name=li.xpath('string(div/div[3]/a/em)')
            if not name:
                continue
            href=li.xpath('div/div[3]/a/@href')[0]
            if len(href)<30:
                href='https:'+href
            price=li.xpath('string(div/div[2])').strip()
            title=li.xpath('div/div[3]/a/@title')[0]
            pinglun=li.xpath('string(div/div[4])').strip()
            blank=li.xpath('string(div/div[5])').strip()
            label=li.xpath('string(div/div[6])').replace('\n','').replace('\t','').replace('    ','|')
            data={
                'name':name,
                'href':href,
                'price':price,
                'title':title,
                'pinglun':pinglun,
                'blank':blank,
                'label':label,
            }
            collection.insert_one(data)
        print('数据添加成功')
        global Index
        while Index<5:
            next=wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='pn-next']")))
            next.click()
            Index+=1
            get_info()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    url='https://search.jd.com/Search?keyword=python&enc=utf-8&wq=python&pvid=74bb714609134b668f2dd929db70cecb'
    driver.get(url)
    get_info()
    driver.close()