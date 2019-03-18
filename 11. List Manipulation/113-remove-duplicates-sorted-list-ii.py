"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return None 
        if not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        compare = dummy
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                val = curr.val 
                while curr and val == curr.val:
                    curr = curr.next
                compare.next = curr
            else:
                curr = curr.next
                compare = compare.next
        return dummy.next
            
