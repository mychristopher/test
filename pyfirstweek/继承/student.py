#！/usr/bin/python
# -*- coding: utf-8 -*-
from person import Person

class Student(Person):
    def __init__(self,name,age,money, stuId):
        #调用父类中的__init__
        super(Student,self).__init__(name,age, money)
        #子类可以有自己独有的属性
        self.stuId = stuId
"""
    def stuFunc(self):
        print(self.__money)
"""