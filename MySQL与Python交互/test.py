#！/usr/bin/python
# -*- coding: utf-8 -*-
from cyfsql import cyfSql

s = cyfSql("localhost","root","7022544qx","test")

res = s.get_all("select * from bandcard where money > 400")

for row in res:
    print("%d--%d" % (row[0], row[1]))