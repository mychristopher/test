#！/usr/bin/python
# -*- coding: utf-8 -*-


def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0]!="1":
        return False
    elif str[1:3]!="30"and str[1:3]!="31"and str[1:3]!="39":
        return False
    for i in range(3,11):
        #print(str[i])
        if str[i]< "0" or str[i] > "9":
            return False
    return True

print(checkPhone("13912345678"))
print(checkPhone("139123456781"))
print(checkPhone("13912345a78"))
print(checkPhone("23912345678"))
print(checkPhone("19012345678"))
