#！/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

#拿到driver
driver=webdriver.Firefox()
#跳转网页
driver.get("http://xdclass.ke.qq.com/")

print(driver.title)

sleep(3)

driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[2]/div[3]/a/img").click()

print(driver.title)