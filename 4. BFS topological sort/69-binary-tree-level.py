from collections import deque
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
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        # if not root:
        #     return []

        # queue = [root]
        # results = []
        # while queue:
        #     next_queue = []
        #     results.append([node.val for node in queue])
        #     for node in queue:
        #         if node.left:
        #             next_queue.append(node.left)
        #         if node.right:
        #             next_queue.append(node.right)
        #     queue = next_queue
        # return results
        if root is None:
            return []
            
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result         