class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        # time excceed, need to reduce looping by keeping only max number
        
    #     if not nums or len(nums) == 1:
    #         return None 
    #     if len(nums) == 2:
    #         return nums[0] + nums[1]
    
    #     res = -sys.maxsize - 1

    #     for i in range(1, len(nums)):
    #         left = self.calculateMax(nums[:i])
    #         right = self.calculateMax(nums[i:])
    #         res = max(res, left + right)
    #     return res
    
    # def calculateMax(self, nums):
    #     temp = 0
    #     maxVal = -sys.maxsize - 1
    #     for num in nums:
    #         temp += num 
    #         maxVal = max(maxVal, temp)
    #         if temp <= 0:
    #             temp = 0
    #     return maxVal
    
    
        leftArray = nums[:]
        rightArray = nums[:]
        n = len(nums)
        
        left = nums[:]
        right = nums[:]
        maxnum = -sys.maxsize - 1
        
        for i in range(1, n):
            left[i] = max(nums[i] + left[i - 1], nums[i])
            leftArray[i] = max(leftArray[i - 1], left[i])
        for i in range(n - 2, -1, -1):
            right[i] = max(nums[i] + right[i + 1], nums[i])
            rightArray[i] = max(rightArray[i + 1], right[i])
        for i in range(n - 1):
            maxnum = max(maxnum, leftArray[i] + rightArray[i + 1])
        return maxnum
        