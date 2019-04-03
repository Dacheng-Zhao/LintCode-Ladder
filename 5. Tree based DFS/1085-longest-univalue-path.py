"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: 
    @return: the length of the longest path where each node in the path has the same value
    """
    def longestUnivaluePath(self, root):
        # Write your code here
        if not root:
            return 0
        self.res = 0
        self.DFS(root)
        return self.res
        
    
    def DFS(self, root):
        if not root:
            return 0 
        left = 0
        right = 0
        p1 = self.DFS(root.left)
        p2 = self.DFS(root.right)
        if root.left and root.left.val == root.val:
            left = p1 + 1 
        if root.right and root.right.val == root.val:
            right = p2 + 1 
        self.res = max(self.res, left + right)
        return max(left, right)
