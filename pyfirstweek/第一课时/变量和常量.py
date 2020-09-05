#！/usr/bin/python
# -*- coding: utf-8 -*-
age=18

age=28
del age
print("age = ",age)

#程序自上而下顺序执行（面向过程）
num1=int(input("请输入一个数字"))
num2=int(input("请再输入一个数字"))

print("num1 + num2 =",num1 + num2)

#查看变量的类型
print(type(age))
#查看变量的地址
print(id(age))

#交互式赋值定义变量
num6,num7 =6,7
print(num6,num7)

#浮点数：浮点型由整数部分与小数部分组成，浮点数运算可能会有四舍五入的误差
#求绝对值 abs
#求x的y次方
print(pow(2,5))
#round(x[,n])返回浮点数x的四舍五入的值，如果给出n值，则代表摄入到小数点后n位
print(round(3.456))
print(round(3.456,2))
#math.ceil 向上取整
#math.floor向下取整
#math.modf返回小数部分与整数部分
#math.sqrt开方
#随机数random.choice   从序列的元素中随机挑选一个元素
print(random.choice(range(5)))

#生成一个1~100之间的随机数
r1=random.choice(range(10))+1
print(r1)

#从指定范围内，按指定的基数递增的集合中选取一个随机数
#random.randrange([start,]stop[,stop])

#随机生成一个[0,1)浮点数
print(random.random())

#将序列的所有元素随机排序
random.shuffle(list)

#随机生成一个实数,他在[3,9]范围
print(random.uniform(3,9))