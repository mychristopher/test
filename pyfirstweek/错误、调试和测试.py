#！/usr/bin/python
# -*- coding: utf-8 -*-

#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce

def str2num(s):
    #return int(s)   #这是原来的语句
    try:
        number=int(s)
    except:   #注意这个地方的写法 是在except里面再写一个try except 而不是并且的写except！！有点类似于if else 里面的嵌套if else
        try:
            number=float(s)
        except:
            print("what you input is not a number!!!")
    finally:
        return number

def calc(exp):
    ss = exp.split('+')  #这里是把calc()里面的字符串以+号分割 剩下的都是单个的字符 '100' ，'200' split之后返回的是list
    ns = map(str2num, ss)#这里借助map函数把上面自己定义的str2num函数（也就是把字符转换成整数的函数）依次作用于ss这个由字符串组成的列表！
    return reduce(lambda acc, x: acc + x, ns)  #再使用reduce函数把两个数相加的函数依次作用于一个map返回的可迭代对象（里面全是数字类型的）

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()


#单元测试
'''
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
'''

#对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：

#文档测试
# import re
# m = re.search('(?<=abc)def', 'abcdef')  # 匹配字符串，且紧挨着匹配的字符串之前的字符等于...，才算匹配成功，且不消耗字符串内容
# print(m.group(0))

#对函数fact(n)编写doctest并执行：
def fact(n):
    '''
    Function to get n!
    Example:
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    >>> fact('a')
    Traceback(most recent call last)
        ...
    KeyError: 'a'
    '''
    if n < 1 :
        raise ValueError()
    if n == 1 :
        return 1
    return n * fact(n - 1)

if __name__ == 'main' :
    import doctest
    doctest.testmod()
print(fact(5))
