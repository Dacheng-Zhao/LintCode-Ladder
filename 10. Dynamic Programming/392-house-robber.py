class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0
        if len(A) == 1:
            return A[0]
        if len(A) == 2:
            return max(A[0] + A[1])
            
        dp = [0 for _ in range(len(A))]
        dp[0] = A[0]
        dp[1] = max(A[0], A[1])
        
        for i in range(2, len(A)):
            dp[i] = max(A[i] + dp[i - 2], dp[i - 1])
        return dp[-1]
