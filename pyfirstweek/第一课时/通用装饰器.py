#！/usr/bin/python
# -*- coding: utf-8 -*-

#通用装饰器
def outer(func):
    def inner(*args, **kwargs):
        #添加修改的功能
        print("&&&&&&&&&&&&&&&&&&&&&")
        func(*args, **kwargs)
    return inner

@outer
#函数的参数理论上无限制，但最好不要超过6-7个
def say(name,age):
    print("my name is %s, I am %d years old" %(name ,age))

say("sunck", 18)