#！/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql



db = pymysql.connect("localhost","root","7022544qx","sunck")
#创建一个cursor对象
cursor = db.cursor()

#创建表
sql = 'update bandcard set money=1000 where id=1'
try:
    cursor.execute(sql)
    db.commit()
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()

#断开
cursor.close()
db.close()