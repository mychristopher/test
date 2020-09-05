#！/usr/bin/python
# -*- coding: utf-8 -*-

# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
#
#     def get_grade(self):
#         if self.__score >= 90:
#             return 'A'
#         elif self.__score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
# bart = Student('Bart Simpson', 59)
# print('bart.get_name() =', bart.get_name())
# bart.set_score(60)
# print('bart.get_score() =', bart.get_score())
#
# print('DO NOT use bart._Student__name:', bart._Student__name)

#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
'''
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender    #让gender属性对外部隐藏
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':     #对gender的参数进行有效性判断
            self.__gender = gender
        else:
            raise ValueError('incorrect gender')

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
'''

#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1   #由于实例属性属于各个实例所有，互不干扰；类属性属于类所有，所有实例共享一个属性；
                             #所以为了实现每创建一个实例属性自动增加，这里的count必须是类的count属性，也就是Student.count
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('lisa')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')