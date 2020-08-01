#！/usr/bin/python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

link = driver.find_element_by_id("s-usersetting-top").click()
time.sleep(2)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)

driver.find_element_by_name("prefpanelgo").click()
time.sleep(2)

alert = driver.switch_to.alert

alert_text = alert.text
print(alert_text)
time.sleep(2)

alert.accept()
time.sleep(2)

driver.quit()