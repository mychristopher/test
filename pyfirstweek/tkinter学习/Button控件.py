#！/usr/bin/python
# -*- coding: utf-8 -*-
#！/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter

def func():
    print("caicai is a small sun")
#创建窗口
win = tkinter.Tk()
#设置标题
win.title("caicai")

#设置大小和位置
win.geometry("400x400+200+20")

button1 = tkinter.Button(win,text="太阳",command=func,
                        width=5,height=1)
button1.pack()

button2 = tkinter.Button(win,text="月亮",command=lambda:print("caicai is a small moon")
                        )
button2.pack()
button3 = tkinter.Button(win,text="退出",command=win.quit)
button3.pack()
win.mainloop()