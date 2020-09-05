#！/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到driver
driver=webdriver.Firefox()
#跳转网页
driver.get("https://home.firefoxchina.cn/")

print(driver.title)

sleep(2)

#定位鼠标移动到上面的元素
menu_ele=driver.find_element_by_css_selector("li.site-multiple:nth-child(4) > a:nth-child(1)")
ActionChains(driver).move_to_element(menu_ele).perform()

#选中子菜单
sub_menu_ele=driver.find_element_by_css_selector("li.site-multiple:nth-child(4) > div:nth-child(2) > a:nth-child(1)")
sleep(2)

sub_menu_ele.click()