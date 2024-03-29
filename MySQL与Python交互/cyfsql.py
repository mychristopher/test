#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

import pymysql

class cyfSql():
    def __init__(self,host,user,passwd,dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    def connet(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.dbName)
        self.cursor = self.db.cursor()
    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self,sql):
        res = None
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")
        return res
    def get_all(self,sql):
        res = ()
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")
        return res

    def insert(self,sql):
        return self.__edit(sql)
    def update(self,sql):
        return self.__edit(sql)
    def __delete(self):
        return self.__edit(sql)

    def __edit(self):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("事物提交失败")
            self.db.rollback()
        return count

