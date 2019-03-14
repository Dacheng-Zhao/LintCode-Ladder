class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        if n == 0:
            return []
        
        self.res = []
        self.DFS('', 0, n, 0, 0)
        return self.res
        
    def DFS(self, string, num, n, left, right):
        if num == n * 2:
            self.res.append(string)
        
        if left < n:
            self.DFS(string + '(', num + 1, n, left + 1, right)
        if right < left:
            self.DFS(string + ')', num + 1, n, left, right + 1)
