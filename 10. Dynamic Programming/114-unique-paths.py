class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        
        for i in range(m):
            dp[0][i] = 1
        
        for j in range(n):
            dp[j][0] = 1 
            
        for x in range(1, m):
            for y in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[n-1][m-1]
