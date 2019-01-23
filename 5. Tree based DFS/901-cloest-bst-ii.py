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
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        if not root:
            return []
            
        self.diction = {}
        diffSet = []
        result = []
        self.DFS(root, target)
        for i in self.diction:
            diffSet.append(i)
        diffSet.sort()
        for j in range(k):
            result.append(self.diction[diffSet[j]])
        return result
        
        
    def DFS(self, root, target):
        if not root:
            return
        
        diff = abs(target - root.val)
        self.diction[diff] = root.val
        
        self.DFS(root.left, target)
        self.DFS(root.right, target)
        
        
    
                
        
                
            
                
        