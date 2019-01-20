"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        # if not root:
        #     return []
        
        # result = []
        # queue = [(root, '')]
        
        # while queue:
        #     node, strr = queue.pop()
        #     if not node.left and not node.right:
        #         result.append(strr + str(node.val))
        #     if node.left:
        #         queue.append((node.left, strr + str(node.val) + '->'))
        #     if node.right:
        #         queue.append((node.right, strr + str(node.val) + '->'))
        # return result
        
        # DFS 
        if not root:
            return []
            
        result = []
        self.DFS(root, [str(root.val)], result)
        return result
        
    def DFS(self, root, path, result):
        if not root.left and not root.right:
            result.append('->'.join(path))
            return
        if root.left:
            path.append(str(root.left.val))
            self.DFS(root.left, path, result)
            path.pop()
        if root.right:
            path.append(str(root.right.val))
            self.DFS(root.right, path, result)
            path.pop()
        