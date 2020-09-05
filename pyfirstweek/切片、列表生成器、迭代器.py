#！/usr/bin/python
# -*- coding: utf-8 -*-

#切片
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
# -*- coding: utf-8 -*-
'''
def trim(s):
    if s == '':
        return s
    while s[:1] ==' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

s1 = '  sdad   sda  '
s2 = trim(s1)
print(s2)
'''

#迭代
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
'''
def findMinAndMax(L):
    if not L:   #判断列表为空，返回两个空值（python中非空即为真,空即为假,因此也常用来判断变量是否为空）
        return (None, None)
    nmin = nmax = L[0]
    for i in L:
        if i < nmin:
            nmin = i
        elif i > nmax:
            nmax = i
    return (nmin,nmax)

L1 = [17, 9, 17, 13, 6]
print(findMinAndMax(L1))
'''

#列表生成器
#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s , str)]

print(L2)
'''

#生成器
#斐波拉契数列
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
'''

#杨辉三角
def triangles(n):
    a = [1]
    index = 0
    while index < n:
        yield a
        a = [a[x] + a[x+1] for x in range(len(a)-1)]
        a.insert(0,1)
        a.append(1)
        index += 1

g = triangles(10)
for i in g:
    print(i)