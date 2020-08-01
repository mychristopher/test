# ！/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from module import Mail

driver = webdriver.Chrome()
driver.get("http://www.126.com")

mail = Mail(driver)

mail.login("username", "1234567")

sleep(5)

mail.logout()

driver.quit()
