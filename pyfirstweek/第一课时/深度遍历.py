#！/usr/bin/python
# -*- coding: utf-8 -*-
import os

def getALLDirDE(path):
    stack = []
    stack.append(path)

    #处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        #从栈里取出数据
        #[]
        dirPath = stack.pop()
        #print(dirPath)
        #目录下所以有文件
        filesList = os.listdir(dirPath)
        #print(filesList)
        #处理每一个文件，如果是普通文件打印出来，如果是目录则将该目录的地址压栈
        for fileNmae in filesList:
            fileAbsPath = os.path.join(dirPath, fileNmae)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录:" + fileNmae)
                stack.append(fileAbsPath)
            else:
                #打印普通文件
                print("普通:" + fileNmae)


getALLDirDE(r"C:\Users\Administrator\Desktop\Python代码练习")