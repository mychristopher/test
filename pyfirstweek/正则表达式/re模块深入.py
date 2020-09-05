#！/usr/bin/python
# -*- coding: utf-8 -*-
import re

#字符串切割

str1 = "caicai  is a small sun"
print(str1.split(" "))
print(re.split(r" +",str1))

"""
re.finditer函数
原型：search(pattern, string, flags=0)
参数：
patter:匹配的正则表达式
string:要匹配的字符串
flags：标识位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，但返回的是一个迭代器

字符串的替换和修改：
re.sub()
sub(pattern, repl, string, count=0, flags=0)
re.subn()
subn(pattern, repl, string, count=0, flags=0)
pattern:正则表达式（规则）
repl:   指定用来替换的字符串
string:  目标字符串
count:    最多替换次数
功能：   在目标字符串中，以正则表达式的规则匹配字符串，再把他们天换成指定的字符串。可以指定替换次数，如果不指定，替换所有的匹配字符串

区别：前者返回一个被替换的字符串，后者返回一个远足，第一个元素表示被替换的字符串，第二个元素表示被替换的次数


分组：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能。用()表示的就是提取分组

编译：当我们使用正则表达式时，re模块会：
1、编译正则表达式，如果正则表达式不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern,flags=0)
pattern:要编译的正则表达式

re_telephon.match(string)
re_telephon.search(string)
"""

str3 = "caicai is a good woman!caicai is a nice woman!caicai is a wondeful woman!"
d = re.finditer(r"(caicai)",str3)
while True:
    try:
        l = next(d)
        print(d)
    except StopIteration as e:
        break

str5 = "caicai is good good good sun!"
print(re.sub(r"(good)","nice",str5))
print(re.subn(r"(good)","nice",str5))

str6 = "010-52367846"
m = re.match(r"(?P<first>\d{3})-(?P<last>\d{8})",str6)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

pat = r"^1(([3578]\d)|(47))\d{8}$"
print(re.match(pat,"13600000000"))
re_telephon = re.compile(pat)
print(re_telephon.match("13600000000"))