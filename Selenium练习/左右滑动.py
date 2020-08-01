#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.get("https://www.helloweba.net/demo/2017/unlock/")

# 定位滑块
slider = driver.find_element_by_class_name("slide-to-unlock-handle")
action = ActionChains(driver)
action.click_and_hold(slider).perform()  # click_and_hold()单击并按下鼠标左键

for index in range(200):
    try:
        action.move_by_offset(5, 0).perform()  # move_by_offset()移动鼠标,第一个参数为x坐标距离，第二个参数为y坐标距离
    except UnexpectedAlertPresentException:
        break
    action.reset_actions()  # 重置action
    sleep(0.1)  # 等待停顿时间

# 打印警告框提示
success_text = driver.switch_to.alert.text
print("success_text")