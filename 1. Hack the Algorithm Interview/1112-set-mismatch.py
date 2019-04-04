class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        # Write your code here
        numsDict = {}
        duplicated = 0
        missing = 0
        for i in range(len(nums)):
            if nums[i] not in numsDict:
                numsDict[nums[i]] = i + 1
            else:
                duplicated = nums[i]
        
        for i in range(1, len(nums) + 1):
            if i not in numsDict:
                missing = i 
        return [duplicated, missing]
