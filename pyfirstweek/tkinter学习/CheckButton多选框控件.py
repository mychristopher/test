#！/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter

#创建窗口
win = tkinter.Tk()
#设置标题
win.title("caicai")
def updata():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "caicai\n"

    #清除text中的所有内容
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,message)
#设置大小和位置
win.geometry("400x400+200+20")
#要绑定的变量
hobby1 = tkinter.BooleanVar()
#多选框
check1 = tkinter.Checkbutton(win,text="money",variable=hobby1,command=updata)
check1.pack()
hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win,text="power",variable=hobby2,command=updata)
check2.pack()
hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win,text="caicai",variable=hobby3,command=updata)
check3.pack()

text = tkinter.Text(win,width=50,height=5)
text.pack()

win.mainloop()