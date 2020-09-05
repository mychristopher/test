#！/usr/bin/python
# -*- coding: utf-8 -*-
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x, y: x * y, L)
L3 = [7, 9, 6, 3, 5, 9]
L4 = prod(L3)
print(L4)

def str2float(s):
   def fn(x, y):
        return x * 10 + y
   def char2num(s):
         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]     #下表索引
   return reduce(fn, map(char2num, s.replace(".","")))
s7="1234.567"
if s7.find(".")!=-1:
     print('str2float(\'%s\') ='%s7, str2float(s7)/pow(10,(len(s7)-s7.find(".")-1)))
else:
    print('str2float(\'%s\') =' %s7, str2float(s7))     #为整数


#求素数
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
  N=[]
  while n!=0:
    N.append(n%10)
    n=n//10
  return N==N[::-1]
output = filter(is_palindrome, range(120, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#排序
#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=by_name))
print(L)   #L不变

#再按成绩从高到低排序：
def by_score(t):
    return t[1]     #列表的每一个元组作为函数的一个参数，取下标索引1为基准
print(sorted(L, key=by_score))  #L不变
print(L)
