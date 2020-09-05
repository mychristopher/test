#！/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到driver
driver=webdriver.Firefox()
#跳转网页
driver.get("https://home.51cto.com/index/?reback=https%3A%2F%2Fedu.51cto.com%2Fcenter%2Fuser%2Findex%2Flogin-success%3Fsign%3D4938VQgGBFQJAFZVAVVbA1UBBgVUDwVWWQVRAAZZEE1HFVtKF1NQERcFVwZFX01SW1RNAFJXR1UTS1ZdR0MXXBgTEgBKGVMBTR0VEURUGhxXVhcRRFwBBARS%26client%3Dweb")

print(driver.title)

sleep(3)

#登陆框
login_ele=driver.find_element_by_css_selector("#login-wechat > div:nth-child(3) > a:nth-child(1)")

#触发点击事件
ActionChains(driver).click(login_ele).perform()

#查找输入框，输入账号密码，输入框需要提前清理
driver.find_element_by_id("loginform-username").clear()
driver.find_element_by_id("loginform-username").send_keys("18511997515")

driver.find_element_by_id("loginform-password").clear()
driver.find_element_by_id("loginform-password").send_keys("cyf1234567")

#查找登录按钮
login_btn_ele=driver.find_element_by_css_selector(".loginbtn")

#触发点击事件
login_btn_ele.click()

#判断是否登录成功  鼠标移动上面，判断弹窗字符
user_info_ele=driver.find_element_by_css_selector("li.fr:nth-child(11) > a:nth-child(1)")

sleep(1)

#触发hover事件
ActionChains(driver).move_to_element(user_info_ele).perform()

#获取用户名的元素
user_name_ele=driver.find_element_by_css_selector("div.More:nth-child(4) > a:nth-child(5)")

print("====测试结果====")
print(user_name_ele.text)

name=user_name_ele.text

if name==u"个人中心":
    print("login ok")
else:
    print("login fail")