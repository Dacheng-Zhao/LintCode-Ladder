class Solution:
    # sorted array leetcode 26
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        l = 0
        r = 1
        
        while r < len(nums):
            if nums[l] == nums[r]:
                nums.pop(l)
            else:
                l += 1
                r += 1
                
                
                