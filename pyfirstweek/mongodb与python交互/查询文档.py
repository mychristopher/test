#！/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo

#连接服务器
conn =MongoClient("localhost",27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

#查询文档

#查询部分文档
'''
res = collection.find({"age":{"$gt":9}})
for row in res:
    print(row)
'''
#查询所有文档
'''
res = collection.find()
for row in res:
    print(row)
'''

#统计查询
'''
res = collection.find({"age":{"$gt":9}}).count()
print(res)
'''

#根据id查询(导入库)
'''
res = collection.find({"_id":ObjectId("5c8751bc77f94a64a82a9412")})
print(res[0])
'''

'''
#排序
#res = collection.find().sort("age")   #升序
res = collection.find().sort("age",pymongo.DESCENDING)
for row in res:
    print(row)
'''

#分页
res = collection.find().skip(3).limit(5)
for row in res:
    print(row)

#断开
conn.close()