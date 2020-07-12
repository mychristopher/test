#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

#for 循环
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello, %s!' % name)

#while 循环

L = ['Bart', 'Lisa', 'Adam']
i = 0
while i < len(L):
    print('Hello, %s!'% L[i])
    i = i + 1

#break语句
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue语句
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)