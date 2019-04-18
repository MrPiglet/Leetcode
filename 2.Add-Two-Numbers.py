'''
@author: Piglet
@time: 2019-04-18
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    	res = ListNode(0)
    	r = res
    	temp = 0
    	add = 0
    	rem = 0
    	while l1 or l2 or add:
    		a = l1.val if l1 else 0
    		b = l2.val if l2 else 0
    		temp = add + a + b
    		rem = temp % 10
    		r.next = ListNode(rem)
    		add = temp // 10
    		r = r.next
    		if l1:
    			l1 = l1.next
    		if l2:
    			l2 = l2.next
    	return res.next