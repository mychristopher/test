#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.save_screenshot("./baidu_img.png")
driver.quit()