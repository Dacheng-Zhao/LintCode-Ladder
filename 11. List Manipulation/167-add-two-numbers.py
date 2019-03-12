"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        
        dummy = curr = ListNode(0)
        carry = 0
        
        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            
            carry += val1 + val2
            curr.next = ListNode(carry % 10)
            carry //= 10 
            curr = curr.next
        
        if carry == 1:
            curr.next = ListNode(1) 
        return dummy.next
                

