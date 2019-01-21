"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    a = False
    b =  False
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        
        # if not root:
        #     return None
        
        
        # left = self.lowestCommonAncestor3(root.left, A, B)
        # right = self.lowestCommonAncestor3(root.right, A, B)
        
        
        # if root == A:
        #     self.a = True
        
        # if root == B:
        #     self.b = True
        
        # if self.a and self.b:
            
        #     if left and right or root in (A, B):
        #         return root
        
        # # if not self.a or not self.b:
        # #     print('a is', self.a)
        # #     print('b is ', self.b)
        # #     return None
        
        #     if not left:
        #         return right
            
        #     if not right:
        #         return left
        
        # return None
        
        if not root or not A or not B:
            return None
            
        self.a = False
        self.b = False
        
        result = self.DFS(root, A, B)
        
        if self.a and self.b:
            return result
        return None
            
    def DFS(self, root, A, B):
        if not root:
            return None
            
        left = self.DFS(root.left, A, B)
        right = self.DFS(root.right, A, B)
        
        if root == A:
            self.a = True
            
        if root == B:
            self.b = True
        
        if (left and right) or root in (A, B):
            return root
            
        if not left:
            return right
        
        if not right:
            return left
        
    
    # def lowestCommonAncestor3(self, root, A, B):
    #     # null case
    #     if not root or not A or not B:
    #         return None

    #     # parameter indicates if A/B is in tree
    #     self.foundA = False
    #     self.foundB = False

    #     # find LCA
    #     lca = self.findLCA(root, A, B)

    #     # check if A and B in tree
    #     if self.foundA and self.foundB:
    #         return lca
    #     return None

    # # helper function to find LCA, return None/A/B
    # def findLCA(self, node, A, B):
    #     # null case
    #     if not node:
    #         return None

    #     # get left/right subtree's LCA
    #     left_lca = self.findLCA(node.left, A, B)
    #     right_lca = self.findLCA(node.right, A, B)

    #     # if node is A/B, found A/B
    #     if node is A:
    #         self.foundA = True
    #     if node is B:
    #         self.foundB = True

    #     # check if node is A or B or left/right LCA is not None 
    #     if node in (A,B) or (left_lca and right_lca):
    #         return node
    #     return left_lca or right_lca or None
    
    # def lowestCommonAncestor3(self, root, A, B):
    #     # write your code here
    #     a, b, lca = self.helper(root, A, B)
    #     if a and b:
    #         return lca
    #     else:
    #         return None

    # def helper(self, root, A, B):
    #     if root is None:
    #         return False, False, None
            
    #     left_a, left_b, left_node = self.helper(root.left, A, B)
    #     right_a, right_b, right_node = self.helper(root.right, A, B)
        
    #     a = left_a or right_a or root == A
    #     b = left_b or right_b or root == B
        
    #     if root == A or root == B:
    #         return a, b, root

    #     if left_node is not None and right_node is not None:
    #         return a, b, root
    #     if left_node is not None:
    #         return a, b, left_node
    #     if right_node is not None:
    #         return a, b, right_node

    #     return a, b, None
        
        
        