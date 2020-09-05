#！/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

#拿到driver
driver=webdriver.Firefox()
#跳转网页
driver.get("http://xdclass.ke.qq.com/")

print(driver.title)

driver.find_element_by_css_selector("div.full-course-item:nth-child(2) > a:nth-child(1) > img:nth-child(1)").click()

print(driver.title)