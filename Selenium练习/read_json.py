#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

import json

with open("./user_info.json", "r") as f:
    data = f.read()

user_list = json.loads(data)
print(user_list)