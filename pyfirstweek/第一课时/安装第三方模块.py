#！/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image

#打开图片
im = Image.open("1.jpg")
#查看图片的信息
print(im.format,im.size,im.mode)

#设置图片的大小
im.thumbnail((150,100))

#保存成相信图片
im.save("temp.jpg","JPEG")

