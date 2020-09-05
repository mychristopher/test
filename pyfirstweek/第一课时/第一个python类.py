#！/usr/bin/python
# -*- coding: utf-8 -*-
#类：一种数据类型。本身并不占内存空间，跟所学过的number，string，boolean等类似。用类创建实例化对象（变量），对象占内存空间
#格式：class  类名（父类列表）:
#          属性(变量)
#          行为（方法）(函数)

#     object：基类，超类，所有类的父类，一般没有合适的父类就写object
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
