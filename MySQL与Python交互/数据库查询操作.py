#！/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql
#detchone()
#功能：或取下一个查询结果集，结果集是一个对象
#fetchall()
#功能：接收全部的返回行
#rowcount:是一个只读属性，返回execute()方法影响的行数


db = pymysql.connect("localhost","root","7022544qx","sunck")
#创建一个cursor对象
cursor = db.cursor()

#创建表
sql = 'select * from bandcard where money > 400'
try:
    cursor.execute(sql)

    reslist = cursor.fetchall()
    for row in reslist:
        print("%d--%d" %(row[0],row[1]))
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()

#断开
cursor.close()
db.close()