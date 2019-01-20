"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if not root:
            return None
            
        self.temp = None
        self.DFS(root)
    
    def DFS(self, root):
        if not root:
            return None
        
        self.DFS(root.right)
        self.DFS(root.left)
        
        root.right = self.temp
        root.left = None
        self.temp = root