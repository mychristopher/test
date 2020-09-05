# -*- coding: utf-8 -*-

#调用函数：
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1 = 255
n2 = 1000

n=[n1,n2]
for i in n:
    print("%d用十六进制表示的字符串为：%s"%(i,hex(i)))

#定义函数
'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。

计算平方根可以调用math.sqrt()函数：
'''
# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
	if b**2-4*a*c >= 0:
		x1=((-b+math.sqrt(b**2-4*a*c))/(2*a))
		x2=((-b-math.sqrt(b**2-4*a*c))/(2*a))
		return '%.2f' %x1,'%.2f' %x2
	else:
		print("无解")
print("请分别输入三个数字a,b,c")
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print(quadratic(a,b,c))

#参数
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
#def product(x, y):
#    return x * y
def product(*a):
    s=1
    for n in a:
        s=n*s
    return s
a=[]
m=int(input('你要输入几个数：'))
i=0
while i<m:
    h=int(input('请输入第%d个数：'%(i+1)))
    a.insert(i,h)
    i=i+1
s=product(*a)
print("他们的乘积为：%d"%s)

