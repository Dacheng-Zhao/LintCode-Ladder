"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        return self.DFS(root, A, B)
        
    
    def DFS(self, root, A, B):
        if not root:
            return None
        if root == A or root == B:
            return root
        
        left = self.DFS(root.left, A, B)
        right = self.DFS(root.right, A, B)
        
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left
