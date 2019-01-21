"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        
        balanced, _ = self.height(root)
        return balanced
    
    def height(self, root):
        if not root:
            return True, 0
            
        balanced, left_height = self.height(root.left)
        if not balanced:
            return False, 0
        balanced, right_height = self.height(root.right)
        if not balanced:
            return False, 0
        
        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1