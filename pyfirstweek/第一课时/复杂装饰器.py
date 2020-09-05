#！/usr/bin/python
# -*- coding: utf-8 -*-


#复杂一点的装饰器
def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner

#使用@符号将装饰器应用到函数
@outer   #say = outer(say) 使用@符号将装饰器应用到函数
def say(age):
    print("sunck is %d years old" %(age))

say(-10)

#通用装饰器是什么样？