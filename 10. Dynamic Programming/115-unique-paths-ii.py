class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid or not obstacleGrid[0]:
            return 1 
        
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1 
        
        for j in range(n):
            if obstacleGrid[j][0] == 1:
                break
            dp[j][0] = 1 
        
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                else:
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[n-1][m-1]
