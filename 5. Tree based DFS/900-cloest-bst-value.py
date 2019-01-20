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
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return 0
            
        self.node = root.val
        self.dfs(root, target)
        return self.node
        
        
    def dfs(self, root, target):
        if not root:
            return 0
        
        if abs(target - self.node) > abs(target - root.val):
            self.node = root.val
        if target > root.val:
            self.dfs(root.right, target)
        else:
            self.dfs(root.left, target)



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
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return None
        
        self.node = root.val 
        
        def dfs(root, target):
            if not root:
                return None
            if abs(target - self.node) > abs(target - root.val):
                self.node = root.val
            if target > root.val:
                dfs(root.right, target)
            else:
                dfs(root.left, target)
                
        dfs(root, target)
        return self.node



      
        
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
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
       
        
        if not root:
            return None
            
        upper = root
        lower = root
        #BFS
        while root:
            if target > root.val:
                lower = root
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val
        
        if abs(target - lower.val) > abs(target - upper.val):
            return upper.val
        else:
            return lower.val
        
               
        
        
        
        