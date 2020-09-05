#！/usr/bin/python
# -*- coding: utf-8 -*-
"""
self代表类的实例，而非类

哪个对象调用方法，那么该方法中的self就代表那个对象

self.__class__代表类名_

"""

class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat",food)
    def say(self):
        print("Hello!my name is %s, I am %d years old"%(self.name,self.age))
    def play(a):     #self不是关键字，换成其他标识符也是可以的
        print("play")
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

per1 = Person("tom",20,160,80)
per1.say()
per2 = Person("t",200,160,80)
per2.say()
per1.play()  #他是这个类里面的方法之一
per2.play()