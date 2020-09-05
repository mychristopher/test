#！/usr/bin/python
# -*- coding: utf-8 -*-

#通过窗体找到进程ID、然后找到对应的内存地址、修改内存
#进程模块
import win32process
#系统
import win32con
import win32gui
import win32api
#C语音类型转换
import ctypes
print("*********1")
PROCESS ALL ACCESS(0x000F0000|0x00100000|0xFFF) #位运算
print("*********2")
#找窗体
win = win32gui.FindWindow("MainWindow", "植物大战僵尸中文版")
print("*********3")
#根据窗体找到进程号
hid, pid = win32process.GetWindowThreadPrrocessId(win)
print("*********4")
#以最高权限打开进程
p = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
print("pid = ", pid)
print("*********5")
#加载内核模块
md = ctypes.windll.LoadLibrary("kernel32.dll的路径")
print("*********6")
data = ctypes.c_long()
print("*********7")
#读取内存
md.ReadProcessMemory(int(p), 311944712, ctypes.byref(data), 4, None)
print("*********8")
print("data=", data)
#设置新值
newData = ctypes.c_long(10000)
print("*********9")
#修改
md.WriteProcessMemory(int(p), 311944712, ctypes.byref(newData), 4, None)