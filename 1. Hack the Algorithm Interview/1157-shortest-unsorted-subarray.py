class Solution:
    """
    @param nums: an array
    @return: the shortest subarray's length
    """
    def findUnsortedSubarray(self, nums):
        # Write your code here
        if not nums:
            return []
        compare = nums[:]
        self.quickSort(0, len(nums) - 1, nums)
        left = 0
        right = 0
        for i in range(len(nums)):
            if compare[i] != nums[i]:
                left = i 
                break
        
        for i in range(len(nums)):
            if compare[i] != nums[i]:
                right = i 
        if left == right:
            return 0
        return right - left + 1
    
    def quickSort(self, start, end, nums):
        if start > end:
            return 
        left = start 
        right = end 
        pivot = nums[start + (end - start) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        self.quickSort(start, right, nums)
        self.quickSort(left, end, nums)
