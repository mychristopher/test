#！/usr/bin/python
# -*- coding: utf-8 -*-
num1 = int(input("请输入一个数"))
num2 = int(input("请输入一个数"))
num3 = int(input("请输入一个数"))

max = num1
if num2>num1:
    max = num2
if num3 > max:
    max =num3

print("max =", max)

#  &按位与运算符
#  |按位或运算符
#  ^按位异或运算符
#  ~按位取反运算符
#  <<左移运算符，高位丢弃，低位补零
#  >>右移运算符，

#关系运算符和关系运算表达式
#逻辑运算符  and  or  not
#成员运算符  in   not in
#身份运算符  is   is not
#运算符优先级

#字符串索引str1[1],但是字符串不可变，字符串中的值不可更改
#截取字符串
str1="sunck is a good man!"
str2=str1[6:15]