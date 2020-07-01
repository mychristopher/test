#！/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql


#链接数据库
#参数一：MySQL/ IP
#参数二：用户名
#参数三：密码
#参数四：要链接的数据库名

db = pymysql.connect("localhost","root","7022544qx","sunck")

#创建一个cursor对象
cursor = db.cursor()


sql = "select version()"

#执行MySQL语句
cursor.execute(sql)

#获取返回的信息
data = cursor.fetchone()
print(data)

#断开
cursor.close()
db.close()