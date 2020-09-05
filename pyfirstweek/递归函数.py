#！/usr/bin/python
# -*- coding: utf-8 -*-
'''
汉诺塔的移动可以用递归函数非常简单地实现。

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)

提示：
那么运用递归的思想可知，若想将n号盘放到z轴上，那么必须先将（1，...，n-1）号盘移动到y轴上，此时z轴作为辅助轴。
然后移动n号盘到z轴上，
最后将y轴上的（1，...，n-1）号盘移动到z轴上，此时x轴作为辅助轴。

'''
def hanoi(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        hanoi(n-1,x,z,y)    #把最底层之上的从第一位都放到第二位
        hanoi(1, x, y, z)   #把最底层的从第一位都放到第三位
        hanoi(n-1,y,x,z)    #把最底层之上的从第二位都放到第三位
while True:
    n=int(input("请输入汉诺塔的层数："))
    hanoi(n,"x","y","z")
    break

