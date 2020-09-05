# coding=utf-8

import xlrd

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)

    for rowNum in range(table.nrows):
        rowVale = table.row_values(rowNum)
        for colNum in range(table.ncols):
            if rowNum > 0 and colNum == 0:
                print(int(rowVale[0]))
            else:
                print(rowVale[colNum])
        print("---------------")

    # if判断是将 id 进行格式化
    # print("未格式化Id的数据：")
    # print(table.cell(1, 0))
    # 结果：number:1001.0


if __name__ == '__main__':
    excelFile = 'C:\\Users\Administrator\Desktop\Python代码练习\excel与python交互/demo.xlsx'
    read_xlrd(excelFile=excelFile)