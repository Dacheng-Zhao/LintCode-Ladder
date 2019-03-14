# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        dummy.next = head
        
        while curr.next and curr.next.next:
            curr.next.val, curr.next.next.val = curr.next.next.val, curr.next.val
            curr = curr.next.next
        return dummy.next
        