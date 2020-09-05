#！/usr/bin/python
# -*- coding: utf-8 -*-
"""
格式：  对象名 = 类名（参数列表）     #对象名就是变量名
相当于函数，没有参数，小括号也不能省略

访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值

访问方法
格式：对象名.方法名（参数列表）

"""
class Person(object):
    name = ""
    age = 0
    height = 0
    weight = 0

#方法的参数必须以self当第一个参数,self代表类的实例（某个对象）
    def run(self):
        print("run")
    def eat(self,food):
        print("eat" + food)

#实例化一个对象
per = Person()
print(per)
per.name = "tom"
per.age = 18
per.height = 180
per.weight = 55
print(per.name,per.age,per.height,per.weight)

"""
per.opendoor()
per.fillEle()
per.closeDoor()
"""

per.eat("apple")

"""
构造函数：__init__()    在使用类创建对象的时候自动调用
如果不显示的写出构造函数，默认会自动添加一个空的构造函数
"""
