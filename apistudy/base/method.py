#!/use/bin/env python
#coding:utf-8 

#Author:WuYa


import  requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

class Method:
	def __init__(self):
		self.operationJson=OperationJson()
		self.excel=OperationExcel()

	def post(self,row):
		try:
			r=requests.post(
				url=self.excel.getUrl(row=row),
				data=self.operationJson.getRequestsData(row=row),
				headers=getHeadersValue(),
				timeout=6)
			return r
		except Exception as e:
			raise  RuntimeError('接口请求发生未知的错误')


class IsContent:
	def __init__(self):
		self.excel=OperationExcel()

	def isContent(self,row,str2):
		flag=None
		if self.excel.getExpect(row=row) in str2:
			flag=True
		else:
			flag=False
		return flag