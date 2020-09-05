#！/usr/bin/python
# -*- coding: utf-8 -*-
#质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
i = 2
while i < 100: #限制i的范围
    j = 2
    while j <= i/j: #限制j的范围
        if not(i % j): #如果能整除则进行下面的代码
            break #能整除则跳出,直接进行i=i+1，不是素数不打印
        j = j + 1 #不能整除则j+1继续

    if(j > (i/j)): #加到j大于根号i还没有找到可被i整除的数，则应该满足素数的要求，打印
        print(i, " 是素数")
    i = i + 1

print ("Good bye!")
