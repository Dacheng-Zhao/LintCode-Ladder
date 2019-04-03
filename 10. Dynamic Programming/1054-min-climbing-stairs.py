class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    """
    def minCostClimbingStairs(self, cost):
        # Write your code here
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        
        for i in range(len(cost)):
            dp[i] = min(cost[i] + dp[i - 1], cost[i] + dp[i - 2])
        
        return min(dp[len(cost)  - 2], dp[len(cost) - 1])
