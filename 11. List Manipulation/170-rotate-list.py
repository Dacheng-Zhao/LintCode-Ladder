"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if not head:
            return None 
        n = 0
        dummy = head
        
        while dummy:
            n += 1 
            dummy = dummy.next
        
        k %= n 
        slow = head
        fast = head
        
        while fast.next:
            fast = fast.next
            k -= 1 
            if k < 0:
                slow = slow.next
        
        fast.next = head
        head = slow.next
        slow.next = None
        return head
        
        
