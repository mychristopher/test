#！/usr/bin/python
# -*- coding: utf-8 -*-
import os

def getALLDir(path, sp = ""):
    filesList = os.listdir(path)  #得到当前目录下的所有文件

    #处理每一个文件
    sp += "   "
    for fileName in filesList:
        #判断是否是路径(用绝对路径)
        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录:",fileName)
            #递归调用
            getALLDir(fileAbsPath, sp)
        else:
            print(sp + "普通文件：",fileName)

getALLDir(r"C:\Users\Administrator\Desktop\Python代码练习")