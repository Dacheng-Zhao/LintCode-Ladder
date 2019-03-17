"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if not head:
            return None 
        
        stack = []
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while head:
            if len(stack) < k:
                stack.append(head)
                head = head.next
                if len(stack) == k:
                    while stack:
                        curr.next = stack.pop()
                        curr = curr.next
                    curr.next = head
        return dummy.next


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if not head:
            return None 
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr != None:
            curr = self.reverse(curr, k)
        return dummy.next
        
    
    def reverse(self, listnode, k):
        lastNode = listnode
        for i in range(k + 1):
            if lastNode:
                lastNode = lastNode.next
            if lastNode == None and i != k:
                return None
        
        tail = listnode.next
        current = listnode.next.next
        
        while current != lastNode:
            next = current.next
            current.next = listnode.next
            listnode.next = current
            tail.next = next
            current = next
        return tail
            
            
            
        
