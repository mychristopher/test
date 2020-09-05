"""
#！/usr/bin/python
# -*- coding: utf-8 -*-
import os

print(os.name)
print(os.environ)   #获取环境变量
print(os.environ.get("APPDATA"))   #获取制定环境变量

print(os.curdir)   #获取当前目录
print(os.getcwd()) #获取当前工作目录，即当前python脚本所在目录
print(os.listdir("目录"))   #以列表的形式返回指定目录下的所有的文件
os.mkdir(r"目录")    #在当前目录下创建新目录
os.rmdir("")     #删除目录
print(os.stat(""))  #获取文件属性
os.rename("","")    #重命名
os.remove("")     #删除普通文件
os.system()   #允许shell命令

#有些方法存在os模块里，还有些存在于os.path
print(os.path.abspath(""))   #查看当前的绝对路径
p1 = r""
p2 = ""
print(os.path.join(p1,p2))   #拼接路径，参数2里面开始不要有斜杠

print(os.path.split(path))   #拆分路径
print(os.path.splittxt(path))  #获取扩展名

print(os.path.isdir(path))    #判断是否有目录
print(os.path.isfile(path))   #判断文件是否存在
print(os.path.exists(path))   #判断目录是否存在
print(os.path.getsize(path))   #获得文件大小（字节）
print(os.path.dirname(path))   #获得文件的目录
print(os.path.basename(path))  #文件的目录
#os.rmdir("sunck")
"""