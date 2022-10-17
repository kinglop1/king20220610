# ！/ python38
# -*- coding: utf-8 -*-
"""
    了解有driver的底层运行逻辑
"""
# from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

# driver = webdriver.Chrome()
driver = WebDriver(executable_path='chromedriver')

# driver.get("http://www.jd.com")
driver.execute('get',{'url':'http://baidu.com'})

# # 在输入框输入你想要胡内容
# # 找到输入框,不要用_by_*函数去定位元素
# de = driver.find_element('id','key')
# de.send_keys('king')

de =driver.execute('findElement',{'using':"css selector",
                                       'value':'[id="kw"]',
                                       })['value']
# print(de)
de._execute("sendKeysToElement",{
     'text': "king",
     'value': ""})

# # 找到搜索按钮
# de1 = driver.find_element('xpath','//*[@id="search"]/div/div[2]/button').click()
de2 =driver.execute('findElement',{'using':"xpath",
                                       'value':'//*[@id="su"]',
                                       })['value']
de2._execute("clickElement")
