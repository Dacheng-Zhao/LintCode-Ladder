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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
    #     self.res = []
    #     self.DFS(root)
    #     return self.res 
        
    # def DFS(self, root):
    #     if not root:
    #         return
    #     self.DFS(root.left)
    #     self.res.append(root.val)
    #     self.DFS(root.right)
    
        res = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                res.append(node.val)
                curr = node.right
        return res
    

                