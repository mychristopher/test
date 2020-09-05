#！/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter

#创建窗口
win = tkinter.Tk()
#设置标题
win.title("caicai")

#设置大小和位置
win.geometry("400x400+200+20")

#label:标签控件可以显示文本
#win  父窗体,text:文本内容 ，  bg  背景色  ，fg  字体颜色
#  font  字体，wraplength  指定多宽之后换行,justify   指定怎样对齐
#anchor 位置n e s w 居中center   ne  se，
label = tkinter.Label(win,
                      text = "caicai is a small sun",
                      bg="pink",
                      fg="red",
                      font = ("黑体",20),
                      width=100,
                      height=2,
                      wraplength=1000,
                      justify="left",
                      anchor="center")
#显示出来
label.pack()

win.mainloop()