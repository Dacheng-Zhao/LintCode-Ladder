class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        self.res = []
        self.DFS(s, [])
        return self.res
        
        
    def DFS(self, s, temp):
        if not s:
            self.res.append(temp[:])
            return
        
        for i in range(len(s)):
            if self.isPalin(s[: i + 1]):
                temp.append(s[: i + 1])
                self.DFS(s[i + 1:], temp)
                temp.pop()
            
    def isPalin(self, s):
        return s == s[::-1]