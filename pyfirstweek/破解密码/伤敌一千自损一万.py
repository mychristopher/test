#！/usr/bin/python
# -*- coding: utf-8 -*-
import itertools
import time

#mylist = list(itertools.product([0,1,2,3,4,5,6,7,8,9,],repeat=5))

passwd = ("".join(x) for x in itertools.product("0123456789",repeat=3))
#print(mylist)
#print(len(mylist))
while True:
    try:
        time.sleep(0.5)
        str = next(passwd)
        print(str)
    except StopIteration as e:
        break

