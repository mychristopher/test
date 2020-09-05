#！/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

#连接服务器
conn =MongoClient("localhost",27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

#添加文档
#collection.insert({"name":"lizicheng","age":9,"gender":0,"address":"南京","isDelete":0})
collection.insert({"name":"lizicheng","age":9,"gender":0,"address":"南京","isDelete":0},
                  {"name":"lishim","age":99,"gender":0,"address":"南京","isDelete":0})

#断开
conn.close()