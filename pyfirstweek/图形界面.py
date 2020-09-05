#！/usr/bin/python
# -*- coding: utf-8 -*-

"""

from tkinter import *
import tkinter.messagebox as messagebox

#每一个gui程序bai都有一个称为顶层(toplevel)的窗口du管理器用于管理那zhi些窗口部件，如按钮dao，输入框之类的，这个窗口管理器就是这些下级部件的master，顶级窗口的master是None即，它自己管理自己
class Application(Frame):
    def __init__(self, master=None):        #master=None只是表明app是顶层窗口而已
        Frame.__init__(self, master)        #再调用title这个方法设置title
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()   #pack函数布局的时候，默认先使用的放到上面，然后依次向下排列，默认方式它会给我们的组件一个自认为合适的位置和大小。
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
"""

"""
#5个五角星
from turtle import *

def drawStar(x, y):
    pu()        #pencilup
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)     #表示海龟启动时的运动方向，包含一个输入参数，是角度值
    for i in range(5):
        fd(40)      #turtle.forward(distance)
        rt(144)     #turtle.right(angle),正五角星的角尖是36度,拐度是108度。

for x in range(0, 250, 50):
    drawStar(x, 0)

done()

"""

# 使用递归，可以绘制出非常复杂的图形。例如，下面的代码可以绘制一棵分型树：
from turtle import *

# 设置色彩模式是RGB:
colormode(255)

lt(90)      #turtle.left(angle)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)   #turtle.back(distance)
pendown()
fd(l)   #turtle.forward(distance)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)   #turtle.left
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)   #turtle.right(angle)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")    #设置画笔移动速度,画笔绘制的速度范围[0,10]整数, 数字越大越快

draw_tree(l, 4)

done()
