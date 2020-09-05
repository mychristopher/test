#！/usr/bin/python
# -*- coding: utf-8 -*-
listNum = []

num = 0
while num < 10:
    val = int(input())
    listNum.append(val)
    num += 1
print(listNum)

listNum.sort()

count = listNum.count(listNum[len(listNum) - 1])
c = 0
while c < count:
    listNum.pop()
    c+= 1
print(listNum[len(listNum)-1])