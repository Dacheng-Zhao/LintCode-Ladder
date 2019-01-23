"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
            self.stack = []
            self.help(root)

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        if self.stack == []:
            return False
        else:
            return True
    """
    @return: return next node
    """
    def next(self):
        # write your code here
        n = self.stack.pop()
        self.help(n.right)
        return n

    def help(self, root):
        while root != None:
            self.stack.append(root)
            root = root.left
        