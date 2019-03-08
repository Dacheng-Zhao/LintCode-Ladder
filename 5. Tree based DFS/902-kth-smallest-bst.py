"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        self.k = k 
        self.res = 0
        self.DFS(root)
        return self.res
    
    def DFS(self, root):
        if not root:
            return
        self.DFS(root.left)
        self.k -= 1 
        if self.k == 0:
            self.res = root.val 
        self.DFS(root.right)
        