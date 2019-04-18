'''
@author: Piglet
@time: 2019-04-18
'''

class Solution:
	def twoSum(self, nums:List[int], target:int):
		#Pig 利用哈希表，边遍历数组边向哈希表添加值
		hashtable = {}
		for index, num in enumerate(nums):
			temp = target - num
			if temp in hashtable:
				return [hashtable[temp], index]
			hashtable[num] = index
		return None