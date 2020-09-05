import urllib.request

url = "http://www.baidu.com"
#编码
newUrl2 = urllib.request.quote(url)
print(newUrl2)
#解码
newUrl = urllib.request.unquote(newUrl2)
print(newUrl)
#向制定的URL地址发起请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen(newUrl)

#读取文件的全部内容,会把读取到的数据赋值给一个字符串
#data = response.read()
#data = response.readline()
#读取文件的全部内容,会把读取到的数据赋值给一个列表变量
#data = response.readlines()
#print(data)

#将怕渠道的网页写入文件
#with open(r"C:\Users\Administrator\Desktop\Python代码练习\爬虫\file\file1.html","wb") as f:
    #f.write(data)

#response属性，返回当前环境的有关信息
#print(response.info())

#返回状态码
#print(response.getcode())
#if response.getcode() == 200 or response.getcode() == 304:
     #处理网页信息
#    pass
#返回当前正在爬取的URL地址
#print(response.geturl())


'''
url = r"https://study.163.com/provider/8317180/index.htm"
#编码
newUrl =  urllib.request.unquote(url)
print(newUrl)
#解码
newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)

response = urllib.request.urlopen(newUrl2)
'''