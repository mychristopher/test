#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

with(open("./test.txt","r")) as user_file:
    data = user_file.readlines()

users = []
for line in data:
    user = line[:-1].split(":")     #去掉回车符号
    users.append(user)

print(users)