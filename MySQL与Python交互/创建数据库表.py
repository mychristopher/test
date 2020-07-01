#！/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql



db = pymysql.connect("localhost","root","7022544qx","sunck")
#创建一个cursor对象
cursor = db.cursor()

#检查表是否存在，如果存在则删除
cursor.execute("drop table if exists bandcard")

#创建表
sql = 'create table bandcard(id int auto_increment primary key,money int not null)'
cursor.execute(sql)

#断开
cursor.close()
db.close()