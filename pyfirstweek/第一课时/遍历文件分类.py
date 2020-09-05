#！/usr/bin/python
# -*- coding: utf-8 -*-
import os
import collections

def work(path):
    resPath = r""
    #打开文件
    with open(path, "r") as f:
    #处理每一行数据
        while True:
            lineInfo = f.readline()
            if len(lineInfo) < 5:
                break
            #邮箱字符串
            #laphae11985@163.com
            mailStr = lineInfo.split("----")[0]
            #邮箱类型的目录 path/163
            #print(mailStr)
            fileType = mailStr.split("@")[1].split(".")[0]
            dirStr = os.path.join(resPath, fileType)
            if not os.path.exists(dirStr):
                #不存在，创建
                os.mkdir(dirStr)
            filePath = os.path.join(dirStr, fileType + ".txt")
            with open(filePath, "a") as fw:
                fw.write(mailStr + "\n")

def getALLDirQU(path):
    queue = collections.deque()
    #进队
    queue.append(path)

    #处理队列，当队列为空的时候结束循环
    while len(queue) != 0:
        #从栈里取出数据
        #[]  出队
        dirPath = queue.popleft()
        #print(dirPath)
        #目录下所以有文件
        filesList = os.listdir(dirPath)
        #print(filesList)
        #处理每一个文件，如果是普通文件打印出来，如果是目录则将该目录的地址压栈
        for fileNmae in filesList:
            #合成绝对路径
            fileAbsPath = os.path.join(dirPath, fileNmae)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录:" + fileNmae)
                queue.append(fileAbsPath)
            else:
                #处理文件
                work(fileAbsPath)


getALLDirQU(r"C:\Users\Administrator\Desktop\Python代码练习")