class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        if not nums:
            return 0 
        
        for i in range(len(nums)):
            if i != 0:
                nums[i] += nums[i - 1]
        
        sumDict = { 0 : 1 }
        count = 0
        
        for i in range(len(nums)):
            if nums[i] - k in sumDict:
                count += sumDict[nums[i] - k]
            if nums[i] not in sumDict:
                sumDict[nums[i]] = 1 
            else:
                sumDict[nums[i]] += 1 
        return count
