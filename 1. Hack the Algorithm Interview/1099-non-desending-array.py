class Solution:
    """
    @param nums: an array
    @return: if it could become non-decreasing by modifying at most 1 element
    """
    def checkPossibility(self, nums):
        # Write your code here
        if not nums:
            return False
        count = 0   
        for i in range(len(nums)):
            if i != 0 and nums[i] < nums[i - 1]:
                count += 1 
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
        return count <= 1
            
