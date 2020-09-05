#！/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter

#创建窗口
win = tkinter.Tk()
#设置标题
win.title("caicai")

#设置大小和位置
win.geometry("400x400+200+20")
#绑定变量
e = tkinter.Variable()
#用于显示简单的文本内容
#show   密文显示show="*"

def showInfo():
    print(entry.get())
entry = tkinter.Entry(win,textvariable=e)
entry.pack()

button = tkinter.Button(win,text="按钮",command=showInfo)
button.pack()
#e就代表输入框这个对象
#设置值
e.set("caicai is a small sun")
#取值
print(e.get())
print(entry.get())

win.mainloop()