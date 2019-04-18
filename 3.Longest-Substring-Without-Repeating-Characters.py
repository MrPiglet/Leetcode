'''
@author: Piglet
@time: 2019-04-18
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	hashmap = {}
    	re = 0
    	first = 0 #PIG 重复的第一个值的指针
    	for k, v in enumerate(s):
    		if v in hashmap:
    			first = max(hashmap[v], first)
    		re = max(k - first, re)
    		hashmap[v] = k
    	return re