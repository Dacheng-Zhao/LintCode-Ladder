class Solution:
    """
    @param nums: an array
    @return: the "pivot" index of this array
    """
    def pivotIndex(self, nums):
        # Write your code here
        if not nums:
            return -1 
        # excceed time limit
        # for i in range(len(nums)):
        #     leftSum = sum(nums[:i])
        #     rightSum = sum(nums[i+1:])
        #     if leftSum == rightSum:
        #         return i
        # return -1 
        
        leftSum = 0
        rightSum = sum(nums)
        
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i 
            leftSum += nums[i]
        return -1 
        