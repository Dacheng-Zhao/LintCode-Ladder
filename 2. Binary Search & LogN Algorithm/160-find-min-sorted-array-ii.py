class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    # do not use binary search [1,1,1,1,1,-1,1,1]
    def findMin(self, nums):
        # write your code here
        if not nums:
            return None 
        start = 0
        end = len(nums) - 1
        target = nums[end]
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[start] == nums[end]:
                end -= 1
            elif nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])
    