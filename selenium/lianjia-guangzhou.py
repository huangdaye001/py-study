'''
爬取广州链家网
使用selenium+Firefox（headless）获取页面信息
xpath解析
数据库pymongo
'''
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import pymongo

client=pymongo.MongoClient()
db=client["test"]
collection=db["guangzhouzufang"]

option=Options()
option.add_argument('-headless')
driver = Firefox(firefox_options=option)
driver.set_window_size(1376,768)
wait=WebDriverWait(driver,10)
index=0
def get_info():
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="content__article"]')))
        print('正在爬取%s----------------'%driver.current_url)
        tree=etree.HTML(driver.page_source)
        infos=tree.xpath('//div[@class="content__article"]//div[@class="content__list--item--main"]')
        for info in infos:
            title=info.xpath('p[@class="content__list--item--title twoline"]/a/text()')[0].strip()
            url=info.xpath('p[@class="content__list--item--title twoline"]/a/@href')[0]
            des=info.xpath('string(p[@class="content__list--item--des"])').replace("\n","").replace(" ","")
            brand =info.xpath('string(p[@class="content__list--item--brand oneline"])').strip()
            time=info.xpath('string(p[@class="content__list--item--time oneline"])')
            bottom=info.xpath('string(p[@class="content__list--item--bottom oneline"])').replace("\n","|").replace(" ","")
            data={
                'title':title ,
                'url': url,
                'des':des ,
                'brand': brand,
                'time': time,
                'bottom': bottom,
            }
            collection.insert_one(data)
        print('添加成功')
        global index
        while index<5:
            next=wait.until(EC.presence_of_element_located((By.XPATH,'//a[@class="next"]')))
            next.click()
            index+=1
            get_info()
    except Exception as e:
        print(e)
            
if __name__ == "__main__":
    url='https://gz.lianjia.com/zufang/'
    driver.get(url)
    get_info()
    driver.close()