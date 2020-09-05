#！/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#拿到driver
driver=webdriver.Firefox()
#跳转网页
driver.get("https://www.jd.com/")

try:
    #显性等待
    ele=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.ID,"key"))
    ele.send_keys("iphone")
    print("资源加载成功")
    print(driver.title)
except:
    print("资源加载失败，发送报警邮件或者短信")

finally:
    print("不管有没有成功，都打印，用于资源清理")
    #退出浏览器
    driver.quit()

