class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        self.quickSort(0, len(nums) - 1, nums)
        kreturn = nums[-k:]
        kreturn.reverse()
        return kreturn
    def quickSort(self, start, end, nums):
        if start >= end:
            return
        pivot = nums[start + (end - start) // 2]
        
        left = start
        right = end
        
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