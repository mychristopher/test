#！/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

#拿到driver
driver=webdriver.Firefox()
#跳转网页
driver.get("http://www.baidu.com")

print(driver.title)

driver.find_element_by_link_text("地图").click()
