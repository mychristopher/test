#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 打开搜索设置
link = driver.find_element_by_id("s-usersetting-top").click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id = 'nr']")
print(sel)
sleep(2)

# value="20"
Select(sel).select_by_value("20")
sleep(2)

# <option>每页显示50条</option>
Select(sel).select_by_visible_text("每页显示50条")
sleep(2)

driver.quit()