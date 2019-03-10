# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        res = self.DFS(root)
        return max(res[0], res[1])
        
    def DFS(self, root):
        if not root:
            return 0, 0
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        res = [0, 0]
        # if robber root, then do not robber left and right
        # if not robber root, then add max left and max right
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res
        