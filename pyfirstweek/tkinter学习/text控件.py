#！/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter

#创建窗口
win = tkinter.Tk()
#设置标题
win.title("caicai")

#设置大小和位置
#win.geometry("400x400+200+20")

#文本控件，用于显示多行文本
#height表示现实的行数
scroll = tkinter.Scrollbar()
text = tkinter.Text(win,width=30,height=4)
#side防盗窗提的哪一侧   fill填充
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
#关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
text.pack()
str = '''caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,
caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,
caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,caicai is a small sun,'''
text.insert(tkinter.INSERT,str)
win.mainloop()