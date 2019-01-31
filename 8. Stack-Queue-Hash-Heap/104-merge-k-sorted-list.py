"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from heapq import heappop, heappush
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap = []
        count = 0
        for l in lists:
            node = l
            while node:
                count += 1
                heappush(heap, (node.val, count, node))
                node = node.next
        
        dummy = ListNode(0)
        cur = dummy
        
        while heap:
            cur.next = heappop(heap)[2]
            cur = cur.next
            
        
        return dummy.next
                
            

