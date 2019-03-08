"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: t
    @return: the sum of all left leaves
    """
    def sumOfLeftLeaves(self, root):
        # Write your code here
        if not root:
            return 0
        self.res = 0
        self.DFS(root)
        return self.res
    
    def DFS(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            self.res += root.left.val 
        self.DFS(root.left)
        self.DFS(root.right)
