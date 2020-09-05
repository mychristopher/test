#！/usr/bin/python
# -*- coding: utf-8 -*-
# += a+=b  a=a+b
'''
-=
*=
/=
%=
**=
//=
'''

#彩票系统
import random
num=int(input("请输入您的号码:"))

res=random.choice(range(10))+1

#判断是否中奖  num==res
if num==res:
    print("恭喜您中了500万")
else:
    print("洗洗睡吧")