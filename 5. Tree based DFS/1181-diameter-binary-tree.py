"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        self.res = 0
        self.DFS(root)
        return self.res
        
    def DFS(self, root):
        if not root:
            return 0
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
