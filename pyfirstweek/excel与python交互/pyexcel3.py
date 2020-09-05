# coding=utf-8

import xlrd

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []

    for rowNum in range(table.nrows):
        # if 去掉表头
        if rowNum > 0:
            dataFile.append(table.row_values(rowNum))

    return dataFile


if __name__ == '__main__':
    excelFile = 'C:\\Users\Administrator\Desktop\Python代码练习\excel与python交互/demo.xlsx'
    print(read_xlrd(excelFile=excelFile))