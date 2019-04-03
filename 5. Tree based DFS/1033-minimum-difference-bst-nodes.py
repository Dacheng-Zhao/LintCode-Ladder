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
    @return: the minimum difference between the values of any two different nodes in the tree
    """
    def minDiffInBST(self, root):
        # Write your code here
        if not root:
            return None 
        self.numArray = []
        self.DFS(root)
        self.numArray.sort()
        minval = sys.maxsize
        for i in range(len(self.numArray)):
            if i != 0:
                minval = min(minval, self.numArray[i] - self.numArray[i - 1])
        return minval
    
    def DFS(self, root):
        if not root:
            return
        self.numArray.append(root.val)
        self.DFS(root.left)
        self.DFS(root.right)
        
