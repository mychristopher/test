# ！/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

driver.set_window_size(800, 600)

driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()

js = "window.scrollTo(100,450);"
driver.execute_script(js)

# text = "input text"
# js = "document.getElementById('id').value='" + text +"';"
# driver.execute_script(js)

sleep(10)
driver.quit()
