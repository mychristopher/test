#！/usr/bin/python
# -*- coding: utf-8 -*-
r"""
python自1.5以后增加了re模块，提供了正则表达式

re模块使python语言拥有了全部的正则表达式功能

re.match函数
原型：match(pattern,string,flag=0)

re.I   忽略大小写
re.L   做本地化识别
re.M   多行匹配，影响^和$
re.S   使.匹配包括换行符在内的所有字符
re.U   根据Unicode字符集解析字符，影响\w  \W  \b  \B
re.X   使我们以更灵活的格式理解正则表达式
参数：patter:匹配的正则表达式
string:要匹配的字符串
flags：标识位，用于控制正则表达式的匹配方式
功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，返回None

re.search函数search(pattern, string, flags=0)
原型：search(pattern, string, flags=0)
参数：patter:匹配的正则表达式
string:要匹配的字符串
flags：标识位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回第一个成功的匹配

re.findall函数findall(pattern, string, flags=0)
原型：findall(pattern, string, flags=0)
参数：patter:匹配的正则表达式
string:要匹配的字符串
flags：标识位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回结果列表
"""

import re

#www.baidu.com
print(re.match("www", "www.baidu.com").span())
print(re.match("www", "ww.baidu.com"))
print(re.match("www", "baiwww.du.com"))
print(re.match("www", "Www.baidu.com",flags=re.I))
#扫描整个字符串，返回的是从起始位置成功匹配的

print(re.search("caicai","good man is caicai!caicai is beautiful"))
print(re.findall("caicai","good man is Caicai!caicai is beautiful",flags=re.I))

