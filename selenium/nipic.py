'''
爬取http://www.nipic.com/newpic/1.html图片网站图片下载到本地
selenium+Firefox（headless）
xpath解析
'''
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import requests
import os

option=Options()
option.add_argument('-headless')
driver=Firefox(firefox_options=option)
driver.set_window_size(1366,786)
wait=WebDriverWait(driver,10)
index=0
def down_img(lists):
    for url in lists:
        #http://pic212.nipic.com/pic/20190328/20332082_145434578038_4.jpg获取到的缩略图
        #http://pic212.nipic.com/file/20190328/20332082_145434578038_2.jpg实际图片链接
        url=url.replace("pic/", "file/").replace("4.jpg", "2.jpg")
        try:
            re=requests.get(url)
            content=re.content
        except Exception as e:
            print('获取图片失败%s'%url)
        if not os.path.exists("imgs"):
            os.mkdir("imgs")
        filename=url.split('/')[-1]
        filepath='imgs/'+filename
        with open(filepath,'wb')as fp:
            fp.write(content)
            print('图片%s下载成功'%url)
    global index
    while index<5:
        #获取下一页   因为只是测试只获取6页
        next=wait.until(EC.presence_of_element_located((By.XPATH,'//a[@class="page-turn-page"][last()]')))
        next.click()
        index+=1
        get_content()
def get_content():
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,'//ul[@class="clearfix"]')))
        print('正在爬取%s'%driver.current_url)
        tree=etree.HTML(driver.page_source)
        lists=tree.xpath('//ul[@class="clearfix"]/li//img/@src')
        print('-------------本页图片数：',len(lists),'--------------')
        down_img(lists)
        

    except Exception as e:
        print(e)

if __name__ == "__main__":
    url="http://www.nipic.com/newpic/1.html"

    driver.get(url)
    get_content()
    driver.close()
