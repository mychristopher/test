import pandas as pd
path = 'C:\\Users\Administrator\Desktop\Python代码练习\excel与python交互/demo.xlsx'
data = pd.read_excel(path,None)#读取数据,设置None可以生成一个字典，字典中的key值即为sheet名字，此时不用使用DataFram，会报错
print(data.keys())#查看sheet的名字
for sh_name in data.keys():
    print('sheet_name的名字是：',sh_name)
    sh_data = pd.DataFrame(pd.read_excel(path,sh_name))#获得每一个sheet中的内容
    print(sh_data)

