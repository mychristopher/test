#！/usr/bin/python
# -*- coding: utf-8 -*-
'''
try......except......else
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句n
else:
    语句e
#else语句可有可无
用来检测try语句块中的错误，从而让except语句捕获错误信息并处理
逻辑：当程序执行到try-expect-else语句时
1、如果当try语句执行出现错误，会匹配第一个错误码，如果匹配上就执行对应"语句
2、如果当try"语句t"执行出现错误，没有匹配的异常，错误将会被提交到上一层的try语句，或者到程序的最上层
3、如果当try"语句t"执行else下的"语句e"(你得有)
#使用ecept带着多种异常

BaseException异常基类
错误其实是class（类），所有的错误都继承自BaseExxception，所以在捕获的时候，它捕获了该类型的错误，还把子类一网打尽
跨越多层调用，main调用了func2，func2调用了func1，func1出现了错误，这时只要main捕获到了就可以处理
finally:    #读取文件可以用到，用来出错关闭文件
    语句f
作用:语句t无论是否有错误都将执行最后的语句f
'''

#断言
def func(num,div):

    assert (div!= 0),"div不能为0"
    return num / div

print(func(10,0))