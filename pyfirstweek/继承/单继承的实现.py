#！/usr/bin/python
# -*- coding: utf-8 -*-
from person  import Person
from student import Student
from worker import Worker

per = Person("aa", 1, 2)


stu = Student("tom",18,123456789, 10)
print(stu.name,stu.age,stu.stuId)
stu.run()
print(stu.stuId)
print(stu.getMoney())

wor = Worker("lili",19,123456789)
print(wor.name,wor.age)
wor.eat("apple")

print(per.getMoney)
#print(stu.__money)私有属性
#print(stu.getMoney())  通过继承过来的共有方法间接访问私有属性
