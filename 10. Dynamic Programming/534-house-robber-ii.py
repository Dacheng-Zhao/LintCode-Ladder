class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0 for _ in range(len(nums))]
        
        # include last but not first house 
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        res1 = dp[-1]
        
        # include first but not last house
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        res2 = dp[-2]
        return max(res1, res2)
