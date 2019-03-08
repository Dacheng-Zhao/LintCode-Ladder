"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        self.res = []
        self.temp = []
        self.DFS(root, target)
        return self.res
        
        
        
    def DFS(self, root, target):
        if not root:
            return None
        
        self.temp.append(root.val)
        target -= root.val
        
        if target == 0 and not root.left and not root.right:
            self.res.append(list(self.temp))
            
        self.DFS(root.left, target)
        self.DFS(root.right, target)
        self.temp.pop()