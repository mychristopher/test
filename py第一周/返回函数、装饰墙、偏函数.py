#！/usr/bin/python
# -*- coding: utf-8 -*-
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
'''
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
传入到counter中的变量不能改变,我们只需要传一个不会变的值进去即可.而这个值不一定是常规的变量.
比如下面的cnt设置成0的话,在counter函数中,我们并不能改变cnt的值,但是如果我们传的cnt是一个列表的话,其实本质上传递的是一个地址,
在这个地址上我们可以做任意改变.只要这个列表还是这个列表,他的地址就不会变.利用这种特性,我们就可以随便折腾了.

def createCounter():
    cnt = [0] # 将cnt设定为数组
    def counter():
        cnt[0] = cnt[0]+1 # 修改数组中的元素值
        return cnt[0] # 返回修改的元素值
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
'''

#请用匿名函数改造下面的代码：
'''
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))


L = list(filter(lambda n : n % 2 == 1, range(1, 20)))
'''
#装饰器
'''
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)
'''

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, (end - begin) * 1000))
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

'''
再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
    
又支持：
@log('execute')
def f():
    pass
'''
import functools
def metric(text1,text2):   # 这里不允许写要服务的函数名
    def decorate(fn):      # 要服务的函数名这里写
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('%s %s:' % (text1, fn.__name__))
            fn(*args, **kw)
            print('%s %s.' % (text2, fn.__name__))
        return wrapper
    return decorate

@ metric('begin call','end call')  # r如果在调用装饰器时要个性化传递参数，装饰器函数需要3层嵌套；注意这里不能再写good，已经@了。
def good(x,y):
    print(x+y)
good(2,3)

