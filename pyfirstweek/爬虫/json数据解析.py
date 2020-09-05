#！/usr/bin/python
# -*- coding: utf-8 -*-
"""
概念：一种数据保存的格式
作用：可以保存本地的json文件，也可以将json串进行传输，通常将json成为轻量级的传输方式

json文件组成
{}  代表对象（字典）
[]  代表列表
,    分割两个部分
:    代表键值对

"""
import json

jsonStr = '''{
      "id":371381,
      "img":"http://uft.upupoo.com/anime/371381/8e0443c426e848afb6d14f0ac78e015f.jpg",
      "infoSort":2,
      "infoUrl":"http://bangumi.bilibili.com/anime/24201/play#205485",
      "numName":"",
      "source":"bili",
      "status":1,
      "subImg":"",
      "title":"无聊诗社 第二季",
      "updateCycle":"1",
      "updateMoment":"00:00"
    }'''

#将json格式的字符串转为python数据类型对象
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
#print(jsonData["infomation"]["0"])

#将python数据类型对象转为json格式的字符串
#jsonStr = json.dumps(jsonData)

#读取本地的json文件
path = r"E:\Windows Kits\10\App Certification Kit\JsonManifestSchema.json"
with open(path,"rb") as f:
    data = json.load(f)
    print(data)
    #字典类型
    print(type(data))

#写入json文件
#path2 = r""
#jsonData ={}
#with open(path2,"w") as f:
#    json.dump(jsonData,f)

