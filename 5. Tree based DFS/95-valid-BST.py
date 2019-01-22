"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if not root:
            return True
            
        Max = sys.maxsize
        Min = -sys.maxsize - 1
        return self.DFS(root, Min, Max)
        
    
    def DFS(self, root, Min, Max):
        if not root:
            return True
        if root.val >= Max or root.val <= Min:
            return False
            
        return self.DFS(root.left, Min, root.val) and self.DFS(root.right, root.val, Max)
    