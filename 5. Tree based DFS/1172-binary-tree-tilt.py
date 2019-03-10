"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the tilt of the whole tree
    """
    def findTilt(self, root):
        # Write your code here
        if not root:
            return 0
        self.res = 0
        self.DFS(root)
        return self.res
    
    def DFS(self, root):
        if not root:
            return 0
        
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        
        self.res += abs(left - right)
        return root.val + left + right
