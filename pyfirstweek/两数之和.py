#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 解题思路：反向解法，利用目标和减去其中一个加数，判断另一个加数在不在list


nums = [2, 7, 11, 15]
target = 9

# def twoSum(nums, target):
#     lens = len(nums)
#     j=-1
#     for i in range(1,lens):
#         temp = nums[:i]
#         if (target - nums[i]) in temp:
#             j = temp.index(target - nums[i])
#             break
#     if j>=0:
#         return [j,i]
def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]

print(twoSum(nums, target))
