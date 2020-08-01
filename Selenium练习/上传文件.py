#！/usr/bin/python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver

file_path = os.path.abspath('.')
print(file_path)

driver = webdriver.Chrome()
upload_page = 'file:///'+file_path+'/upload.html'

driver.get(upload_page)

driver.find_element_by_id("file").send_keys(file_path+'test.txt')