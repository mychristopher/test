#！/usr/bin/python
# -*- coding: utf-8 -*-

import random
l = []
for i in range(6):
    alpha = chr(random.randint(65, 90))             # random.randrange(65,91)
    alpha_lower = chr(random.randint(97, 122))      # random.randrange(65.91)
    num = str(random.randint(0, 9))
    ret = random.choice([alpha,num,alpha_lower])
    l.append(ret)
print(''.join(l))