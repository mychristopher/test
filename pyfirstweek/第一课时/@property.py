#！/usr/bin/python
# -*- coding: utf-8 -*-
class Person(object):
    def __init__(self,name,age):
        #属性直接对外暴露
        #限制访问
        self.__age = age
        self.__name = name
    #方法名为受限制的变量去掉双下划线
    @property
    def age(self):
        return self.__age
    @age.setter   #去掉下划线.setter
    def age(self,age):
        if age < 0:
            age = 0
        self.__age = age
"""
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if age < 0:
            age = 0
        self.__age = age
"""

per = Person("cyf",18)

#属性直接对外暴露
#不安全，没有数据的过滤
#per.age = -10
#print(per.age)

#使用现在只访问，需要自己写set和get方法
#per.setAge(15)
#print(per.getAge())

per.age = 111    #相当于调用setAge
print(per.age)    #相当于调用getAge