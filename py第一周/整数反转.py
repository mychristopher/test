#！/usr/bin/python
# -*- coding: utf-8 -*-

# 解题思路
# 1.把数字转换成字符串，再将字符串倒序
# 2.定义一个sign用来决定正负值，如果是负数的话，倒序之前先将 - 符号忽略
# 3.再范围内返回值，超过范围返回0

class Solution:
	def reverse(self, x: int) -> int:
		'''
		真正不会整型溢出的python解法，
		数学方法的pop和append

		'''
		sign = x >= 0  # x正负
		maxInt32 = (1 << 31) - 1  # 准备int32最大值
		res = 0  # 准备结果，初始化为0

		if x == - 1 << 31: return 0  # 若x为负int32最小值，则反转后必定溢出，其余负数情况和正数是对称的
		x = abs(x)  # 所以将x转为正数来处理

		while x != 0:  # 只要还没有pop完
			pop = x % 10  # pop为x的最后一位
			x //= 10  # x去掉最后一位
			# 当result已经大于最大值//10，或者等于int32最大值//10并且当前pop出的值大于7时，必定溢出，返回0
			if res > maxInt32 // 10 or res == maxInt32 // 10 and pop > 7: return 0
			# 如果不溢出，则把pop出的值加进result中
			res = res * 10 + pop
		# 最后返回带正负号的result
		return res if sign else -res

