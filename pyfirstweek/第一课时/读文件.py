#！/usr/bin/python
# -*- coding: utf-8 -*-
#打开文件、读文件、关闭文件
'''
1、打开文件
open(path，flag[,encoding][,errors])
path:要打开文件的路径
flag:打开方式
r  以只读的方式打开文件，文件的描述符放在文件的开头
rb  以二进制格式打开一个文件用于只读，文件的描述符放在文件的开头
r+  打开一个文件用于读写，文件的描述符放在文件的开头
w  打开一个文件只用于写入，如果该文件已存在则会覆盖，如果不存在则创建新文件
wb  打开一个文件值只用于写入二进制，如果该文件已存在则会覆盖，如果不存在则创建新文件
w+  打开一个文件用于读写
a   打开一个文件用于追加，如果文件存在，文件描述符将会放到文件末尾
a+
encoding:编码方式
errors:错误处理

读文件内容

关闭文件

写文件
path = r"路径"
f = open(path,"w")
将信息写入缓存区
f.write("sunck is a good man")

f.flush()   刷新缓存区，直接把内部缓存区的数据立刻写入文件，而不是被动的等待关闭自动刷新缓存区写入
#编码
path = r"路径"
with open(path,"wb",encoding="utf-8") as fi:
    str = "sunck is a good man"
    f1.write(str.encode("utf-8"))
with open(path,"rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8")
    print(newData)
    print(type(newData))
'''
path = r"C:\Users\Administrator\Desktop\python学习文档.txt"
f = open(path,"r",encoding="utf-8",errors="ignore")

#str1 = f.read() #读取文件全部内容 #读完后文件描述符在文件最后、再读为空
#print(str1)

#str2 = f.read(20) #读取指定字符数
#print(str2)

str4 = f.readline() #读取一行，传入数字还是读取指定字符数
print(str4)


#str4 = f.readlines()   读取所有行并返回列表格式；若给定的数字大于0，返回实际size字节所在的行
#print(str4)

f.close()

#修改描述符的位置
#f.seek(0)

'''
#一个完整的过程
try:
    f1 = open(path, "r", encoding="utf-8")
    print(f1.read())
finally:
    if f1:
        f1.close()

#自动关上
with open((path, "r", encoding="utf-8") as f2:
    print(f2.read())
'''