#！/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

#拿到driver
driver=webdriver.Firefox()
#跳转网页
driver.get("http://www.runoob.com/python/python-modules.html")

print(driver.title)

driver.find_element_by_partial_link_text("语句").click()