# ！/usr/bin/python
# -*- coding: utf-8 -*-
# ！/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

element = WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located((By.ID,"kw"))
)
element.send_keys('selenium')
time.sleep(1)
# above = driver.find_element_by_id("s-usersetting-top")
# ActionChains(driver).move_to_element(above).perform()
# time.sleep(3)

# driver.find_element_by_id("kw").send_keys("Selenium")
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys("教程")
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.ENTER)
# time.sleep(1)
# driver.find_element_by_id("kw").clear()
# time.sleep(5)
# driver.find_element_by_id("kw").send_keys("Selenium")
# time.sleep(5)
# driver.find_element_by_id("su").click()
# time.sleep(5)
# search_text = driver.find_element_by_id("kw")
# search_text.send_keys("Selenium")
# time.sleep(2)
# search_text.submit()
# driver.find_element_by_link_text("新闻").click()
# time.sleep(5)
# driver.set_window_size(480, 800)
# time.sleep(5)
# driver.maximize_window()
# time.sleep(5)

# first_url = 'https://www.baidu.com'
# driver.get(first_url)
# time.sleep(3)
#
# second_url = 'https://news.baidu.com'
# driver.get(second_url)
# time.sleep(3)
#
# driver.back()
# time.sleep(3)
#
# driver.forward()
# time.sleep(3)
#
# driver.refresh()
# time.sleep(3)

driver.quit()
