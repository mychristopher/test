#！/usr/bin/python
# -*- coding: utf-8 -*-
from Child import Child

def main():
    c = Child(300,100)
    print(c.money,c.faceValue,c.height)
    c.play()
    c.eat()
    c.func()
    #父类中方法名相同，默认调用的是在括号中排在前面的父类中的方法

if __name__=="__main__":
    main()