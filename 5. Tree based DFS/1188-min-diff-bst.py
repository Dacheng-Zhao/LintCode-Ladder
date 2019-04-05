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
    @return: the minimum absolute difference between values of any two nodes
    """
    def getMinimumDifference(self, root):
        # Write your code here
        if not root:
            return None 
        self.array = []
        self.DFS(root)
        self.array.sort()
        res = sys.maxsize
        for i in range(len(self.array)):
            if i != 0:
                res = min(res, self.array[i] - self.array[i - 1])
        return res
    
    def DFS(self, root):
        if not root:
            return 
        self.array.append(root.val)
        self.DFS(root.left)
        self.DFS(root.right)
    
