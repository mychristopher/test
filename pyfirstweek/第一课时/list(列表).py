#！/usr/bin/python
# -*- coding: utf-8 -*-
list1 = [18,19,20,21,22]
index = 0
sum = 0
while index < 5:
    sum += list1[index]
    index += 1
    if index == 5:
        print("平均年龄:%d" % (sum / 5))

#嵌套最好不要超过三层
#列表组合，列表重复，判断元素是否在列表中，列表截取
#二维列表
list2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list2[2][2])

#列表方法 ，在列表末尾添加新元素
list2.append([12,13,14])
#在末尾一次性追加另一个列表中的多个值
list2.extend([12,13,14])
#在下标处添加一个元素，不覆盖元数据，原数据向后顺延
list2.insert(2,[200,300])
#移除列表中指定下标处的元素(默认移除最后一个元素),并返回删除的数据
list2.pop()
list2.pop(2)
#remove  移除列表中的某个元素第一个匹配的结果
list2.remove(4)
#移除列表中所有的数据
list2.clear
#从列表中找出某个值第一个匹配的索引值
list3 = [1,2,3,4,5,6,7,8,9]
index4=list3.index(3)
#圈定范围
index5=list3.index(3,3,7)
print(index4,index5)

#列表中元素个数
list4 = [1,3,4,5,6,7]
print(len(list4))
#获取列表中的最大最小值
#max()  min()
#查看元素在列表中出现的次数
list3.count(3)

#倒序
list3.reverse()
#排序,升序
list3.sort()
#浅拷贝
list5 = [1,2,3,4,5]
list6 = list5
list6[1]=200  #list5,list6都变
#深拷贝 内存的拷贝
list7=[1,2,3,4,5]
list8=list7.copy()
list8[1]=200  #list8改变，list7不变
#将元祖转成列表
list11 = list((1,2,3,4))
