class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        self.res = []
        temp = []
        self.DFS(n, k, 1, 0, temp)
        return self.res
        
    def DFS(self, n, k, m, p, temp):
        if k == p:
            self.res.append(temp[:])
            return
        
        for i in range(m, n + 1):
            temp.append(i)
            self.DFS(n, k, i + 1, p + 1, temp)
            temp.pop()
            