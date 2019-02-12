class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return None
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        
        for j in range(1, m):
            dp[j][0] = grid[j][0] + dp[j-1][0]
            
        res = dp[0][0]
            
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = grid[x][y] + min(dp[x-1][y], dp[x][y-1])
        return dp[m-1][n-1]