#！/usr/bin/python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

search_windows = driver.current_window_handle
print(search_windows)
time.sleep(10)

# driver.find_element_by_link_text('高考加油').click()
# time.sleep(10)
driver.find_element_by_link_text('登录').click()
time.sleep(10)
driver.find_element_by_link_text('立即注册').click()
time.sleep(10)

all_handles = driver.window_handles
print(all_handles)
time.sleep(10)

for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print(driver.title)
        time.sleep(5)
        driver.find_element_by_name("userName").send_keys('username')
        driver.find_element_by_name('phone').send_keys('18511997515')
        time.sleep(2)

        driver.close()

driver.switch_to_window(search_windows)
print(driver.title)


time.sleep(5)
driver.quit()