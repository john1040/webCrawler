# import requests
#
# res = requests.get('http://pala.tw/js-example/')
# print(res.text)

# from selenium import webdriver
#
# driver = webdriver.PhantomJS(executable_path=r'/Users/Jia-anwang/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
# driver.get('http://pala.tw/js-example/')
# pageSource = driver.page_source
# print(pageSource)
#
# driver.close()


import requests
from bs4 import BeautifulSoup
tag = input("請輸入定位元素，class前面加上.，id前面加上# ")
res = requests.get('http://pala.tw/class-id-example/')
soup = BeautifulSoup(res.text, "lxml")

for drink in soup.select('{}'.format(tag)):
    print(drink.get_text())
