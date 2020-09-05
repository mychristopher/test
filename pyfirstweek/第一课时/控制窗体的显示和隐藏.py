#！/usr/bin/python
# -*- coding: utf-8 -*-
import win32con
import win32gui
import time
import random




'''
下载spy窗口.exe，用于获取qq等软件窗口
QQWin = win32gui.FindWindow("","")  #找出窗体的编号
win32gui.SetWindowPos(QQWin,win32con.HWND_TOPMOST,100,200,300,400)
#控制的窗体，大致方向，位置x，位置y，长度，宽度
win32gui.ShowWindow(QQWin,win32con.SW_SHOW) #显示窗体
win32gui.ShowWindow(QQWin,win32con.SW_HIDE)  #隐藏窗体
'''
'''
整人代码
while True:
    QQWin = win32gui.FindWindow("TXGuiFoundation","QQ")
    win32gui.ShowWindow(QQWin, win32con.SW_HIDE)  # 隐藏窗体
    time.sleep(2)
    win32gui.ShowWindow(QQWin, win32con.SW_SHOW)  # 显示窗体
    time.sleep(1)
'''
#参数1：控制的窗体
#参数2：大致方位，HWND_TOPMOST上方
#参数3、4：位置坐标
#参数5、6：长度、宽度

while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, x, y, 300, 300,win32con.SWP_SHOWWINDOW)
    # 控制的窗体，大致方向，位置x，位置y，长度，宽度


