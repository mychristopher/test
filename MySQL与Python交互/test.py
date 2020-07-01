#！/usr/bin/python
# -*- coding: utf-8 -*-
from caicaisql import caicaiSql

s = caicaiSql("localhost","root","7022544qx","sunck")

res = s.get_all("select * from bandcard where money > 400")

for row in res:
    print("%d--%d" % (row[0], row[1]))