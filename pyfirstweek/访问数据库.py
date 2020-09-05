#！/usr/bin/python
# -*- coding: utf-8 -*-

# SQLite
"""
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
print('rowcount =', cursor.rowcount)
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

# 查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', '1')
# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
"""

"""
# 请编写函数，在Sqlite中根据分数段查找指定的名字：

import os
import sqlite3  # 导入SQLite驱动:

db_file = os.path.join(os.path.dirname(__file__), 'test.db')  # 数据库的创建,当前路径和新建文件组成新的路径
if os.path.isfile(db_file):     # 如果存在这个同名文件的话删除掉
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)     # 连接到SQLite数据库
cursor = conn.cursor()      # 创建一个Cursor:
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')    # 执行一条SQL语句，创建user表:
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")        # 继续执行一条SQL语句，插入一条记录:
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")        # 继续执行一条SQL语句，插入一条记录:
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")        # 继续执行一条SQL语句，插入一条记录:
cursor.close()      # 关闭Cursor:
conn.commit()       # 提交事务:
conn.close()        # 关闭Connection:

import sqlite3  # 导入SQLite驱动:
from operator import itemgetter     #字典列表: itemgetter 函数: 根据某个或某几个字典字段来排序列表

def get_score_in(low, high):
    # 返回指定分数区间的名字，按分数从低到高排序
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select * from user')   # 执行查询语句
    values = cursor.fetchall()      # 获得查询结果集，结果集是一个list，每个元素为一个tuple
    values = sorted(values, key=itemgetter(2))      # 通过sorted 根据分数来对结果集排序，根据第三个域进行排序
    result = []
    for i in values:    # 循环
        if low <= i[2] <= high:     # 筛选
            result.append(i[1])     # 结果
    return result       # 返回

# 测试:
print(get_score_in(80, 95))
print(get_score_in(60, 80))
print(get_score_in(60, 100))
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
"""

"""
# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='7022544qx', database='test')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()

"""

