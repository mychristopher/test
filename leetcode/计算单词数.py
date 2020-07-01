#！/usr/bin/python
# -*- coding: utf-8 -*-
str = input()
#ssadsa dsaj fasjdsa jaj dsaj
str1 = str.strip()
index = 0
count = 0
while index < len(str1):
    while str1[index]!=" ":
        index += 1
        if index == len(str1):
            break
            #结束这个循环
    count += 1
    if index == len(str1):
        break
    while str1[index] == " ":
        index += 1
print (count)