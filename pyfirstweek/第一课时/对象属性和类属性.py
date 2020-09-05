#！/usr/bin/python
# -*- coding: utf-8 -*-
class Person(object):
    #这里的属性实际上属于类属性（用类名来调用）
    name = "person"
    def __init__(self,name):
        #对象属性
        self.name = name

print(Person.name)
per = Person("tom")  #对象属性的优先级高于类属性
print(per.name)
per.age = 18   #只针对当前对象生效，对于类创建的其他对象没有作用(动态地给对象添加对象属性)

print(Person.name)
per2 = Person("lilei")

#不要将对象属性和类属性重名，会屏蔽掉类属性
#以上情况删除对象属性之后才会使用类属性

#定义类的时候，定义一个特殊的属性(__slots__)，可以限制动态添加的属性
