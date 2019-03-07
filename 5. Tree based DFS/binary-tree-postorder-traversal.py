# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
#         self.DFS(root)
#         return self.res
        
#     def DFS(self, root):
#         if not root:
#             return
#         self.DFS(root.left)
#         self.DFS(root.right)
#         self.res.append(root.val)
        res = []
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.right
            else:
                node = stack.pop()
                curr = node.left
        return res[::-1]
        