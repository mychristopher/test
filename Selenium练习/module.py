# ！/usr/bin/python
# -*- coding: utf-8 -*-

class Mail:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.driver.switch_to.frame('x-URS-iframe')
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(username)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("dologin").click()
    def logout(self):
        self.driver.find_element_by_id("退出").click()