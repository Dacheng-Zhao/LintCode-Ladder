class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        presum = 0
        minval = 0
        maxval = -sys.maxsize
        
        for num in nums:
            presum += num 
            maxval = max(maxval, presum - minval)
            minval = min(minval, presum)
        return maxval