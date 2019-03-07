"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
    #     self.res = []
    #     self.DFS(root)
    #     return self.res
    
    # def DFS(self, root):
    #     if not root:
    #         return
    #     self.res.append(root.val)
    #     self.DFS(root.left)
    #     self.DFS(root.right)
    
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
        
