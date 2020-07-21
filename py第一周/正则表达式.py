#！/usr/bin/python
# -*- coding: utf-8 -*-

import re

# test = '010-12345'
# if re.match(r'^\d{3}\-\d{3,8}$', test):
#     print('ok')
# else:
#     print('failed')

'''
s1 = 'a b   c'.split(' ')
print(s1)

s2 = re.split(r'\s+', 'a b   c')    #匹配任意空白字符，等价于 [ \t\n\r\f]。+数量不限
print(s2)

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print(str.split( ));       # 以空格为分隔符，包含 \n
print(str.split(' ', 1 )); # 以空格为分隔符，分隔成两个
'''

# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com

import re

# 先编译好正则
#[\w]+和\w+没有区别，都是匹配数字和字母下划线的多个字符；
re_email = re.compile(r'^[\w]+\.?[\w]+@[\w]+\.com$')
# 正则解释：     字母一个以上 .一个或没有 字母一个以上 @ 字母不限 .com
def is_valid_email(addr):
    if re_email.match(addr):
        return True

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

'''
import re

re_name_of_email = re.compile(r'^<?([\w]+\s*[\w]*)>?\s*[\w]*@[\w]+\.org$')
# 正则解释             <一个或无 字母一个以上 空格不限 字母不限 >一个或无 @ 字母一个以上 .org
#  re?    匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
def name_of_email(addr):
    if re_name_of_email.match(addr):
        return re_name_of_email.match(addr).group(1)

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
'''
