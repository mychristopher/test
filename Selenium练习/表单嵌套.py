#！/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")
sleep(2)

login_frame = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)
sleep(5)

driver.find_element_by_name("email").send_keys("cyf1366254420")
driver.find_element_by_name("password").send_keys("7022544qx")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

sleep(1)

driver.quit()