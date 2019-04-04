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
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """
    def findSecondMinimumValue(self, root):
        # Write your code here
        if not root:
            return -1 
        self.array = []
        self.DFS(root)
        if len(self.array) < 2:
            return -1 
        else:
            self.array.sort()
            return self.array[1]
    
    def DFS(self, root):
        if not root:
            return 
        if root.val not in self.array:
            self.array.append(root.val)
        
        self.DFS(root.left)
        self.DFS(root.right)
