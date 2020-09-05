#！/usr/bin/python
# -*- coding: utf-8 -*-
#迭代器：不但可以作用于for循环，还可以被next（）函数不断调用并返回下一个值，直到最后抛出一个StopIteration错误表示无法继续返回下一个值
#可以被next()函数调用并不断返回下一个值的对象为迭代器(Iterator)
#可以使用isinstance()函数判断一个对象是否是Iterator对象
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance(1,Iterable))
print(isinstance((x for x in range(10)),Iterable))

#转成Iterator对象
a = iter([1,2,3,45,5])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))