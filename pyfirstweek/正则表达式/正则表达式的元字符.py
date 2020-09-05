#！/usr/bin/python
# -*- coding: utf-8 -*-
import re

r"""
匹配单个字符与数字
.   可以匹配除换行符以外的任意字符
[0123456789]   []是字符集合，表示匹配方括号中所有所包含的任意一个字符
[caicai]   匹配'c''a''i'中任意一个字符
[a-z]      匹配任意小小写字母
[A-Z]
[0-9]
[0-9a-zA-Z]   匹配任意的数字和字母
[0-9a-zA-Z_]   匹配任意的数字和字母和下划线
[^cai]         匹配除了cai这几个字母以外的所有字符，
[^0-9]       匹配所有的非数字字符
\d        匹配数字，效果同[0-9]
\D          匹配所有的非数字字符,效果如同[^0-9]  
\w     匹配数字、字母和下划线，效果如同[0-9a-zA-Z_]
\W     匹配非数字、字母和下划线，下效果如同[^0-9a-zA-Z_]
\s    匹配任意的空白符（空格、换行、回车、换页、制表、），效果同[ \f\n\r\t]
\S     匹配任意的非空白符，效果同[^ \f\n\r\t]

锚字符（边界字符）
^   行首匹配，和在[]里的^不是一个意思
$    行尾匹配
\A   匹配字符串的开头，他和^的区别是，\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配其他行的行首
\Z   匹配字符串的结束，他和$的区别是，\A只匹配整个字符串的结束，即使在re.M模式下也不会匹配其他行的行尾
\b   匹配一个单词，以所要的字母为边界
\B   匹配一个单词，以所要的字母不为边界   注意前面加r，区分转义字符

匹配多个字符
(xyz)     匹配小括号内的xyz（作为一个整体去匹配）
x?     匹配0个或者1个x    非贪婪匹配
x*     匹配0个或任意多个x    贪婪匹配
x+     匹配至少一个x     贪婪匹配
x{n}   匹配确定的n个x（n是一个非负整数）
x{n,}  匹配至少n个x    贪婪匹配
x{n,m}   匹配至少n个最多m个x。注意：n<=m
x|y      |表示或，匹配的是x或y

特殊批评
*?   +?   x?  最小匹配，通常都是竟可能多的匹配，可以使用这种解决贪婪匹配
(?:x)     类似（xyz），但不表示一个组


"""

#print(re.findall("[^\d]","caicai is a 6sun"))

#提取caicai......sun
str = "caicai is a good sun!caicai is a nice sun!caicai is a very sun!"
print(re.findall(r"^caicai.*sun$",str))

#注释：   /*  part1   */   /*   part2    */

print(re.findall(r"//*.*?/*/",r"/*  part1   */   /*   part2    */"))

def checkPhone2(str):
    #13912345678
    pat = r"^1(([3578]\d)|(47)\d{8}$"
    res = re.match(pat,str)
    return res

"""
print(checkPhone2("13912345678"))
print(checkPhone2("139123456785"))
print(checkPhone2("1391234a678"))
print(checkPhone2("23912345678"))
"""

checkPhone2("asdsadsadasdadsa13709876543asdsadadasd13599999999sadasdadda")
