"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """
    def reverseStore(self, head):
        # write your code here
        if not head:
            return [] 
        self.res = []
        
        self.DFS(head)
        
        return self.res
       
    def DFS(self, head):
        if not head:
            return 
        
        self.DFS(head.next)
        self.res.append(head.val)
        
