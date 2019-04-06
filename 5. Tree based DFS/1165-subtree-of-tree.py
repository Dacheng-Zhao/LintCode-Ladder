"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """
    def isSubtree(self, s, t):
        # Write your code here
        if not s:
            return t is None 
        
        if s.val == t.val:
            if self.compare(s, t):
                return True 
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    
    def compare(self, sub, t):
        if not sub:
            return t is None 
        if not t or sub.val != t.val:
            return False
        return self.compare(sub.left, t.left) and self.compare(sub.right, t.right)
