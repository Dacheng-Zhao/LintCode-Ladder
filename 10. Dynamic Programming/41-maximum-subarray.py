class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] == nums[0]
        maxval = -sys.maxsize
        res = nums[0]
        
        for i in range(n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(dp[i], res)
        return res
        
#         if not nums or len(nums) == 0:
#             return None
    
#         maxsum = -sys.maxsize
#         temp = 0
        
#         for num in nums:
#             temp += num
#             maxsum = max(maxsum, temp)
#             if temp < 0:
#                 temp = 0
#         return maxsum

        
             
        