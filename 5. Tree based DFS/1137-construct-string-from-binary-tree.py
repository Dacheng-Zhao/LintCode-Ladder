"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t: the root of tree
    @return: return a string
    """
    def tree2str(self, t):
        # write your code here
        if not t:
            return None 
        if not t.left and not t.right:
            return str(t.val) 
        if not t.left:
            return str(t.val) + '()' + '(' + self.tree2str(t.right) + ')'
        if not t.right:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
 