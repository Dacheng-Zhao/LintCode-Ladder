"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
    #     if not root:
    #         return []
    #     self.res = []
    #     self.DFS(root, 0)
    #     left = 0
    #     right = len(self.res) - 1 
    #     while left < right:
    #         self.res[left], self.res[right] = self.res[right], self.res[left]
    #         left += 1 
    #         right -= 1 
    #     return self.res
    
    # def DFS(self, root, level):
    #     if not root:
    #         return
    #     if len(self.res) <= level:
    #         self.res.append([])
    #     self.res[level].append(root.val)
        
    #     self.DFS(root.left, level + 1)
    #     self.DFS(root.right, level + 1)
    
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            new_queue = []
            res.append([n.val for n in queue])
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        left = 0
        right = len(res) - 1 
        while left < right:
            res[left], res[right] = res[right], res[left]
            left += 1 
            right -= 1 
        return res
            
            
