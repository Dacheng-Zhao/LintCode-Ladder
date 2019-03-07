class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
    #     if not nums:
    #         return []
    #     self.quickSort(nums, 0, len(nums) - 1)
    #     return nums
        
    
    # def quickSort(self, A, start, end):
    #     if start >= end:
    #         return
    #     left = start
    #     right = end 
    #     pivot = A[start + (end - start) // 2]
        
    #     while left <= right:
    #         while left <= right and A[left] < pivot:
    #             left += 1 
    #         while left <= right and A[right] > pivot:
    #             right -= 1 
    #         if left <= right:
    #             A[left], A[right] = A[right], A[left]
    #             left += 1 
    #             right -= 1 
    #     self.quickSort(A, start, right)
    #     self.quickSort(A, left, end)
    
        left = 0
        right = len(nums) - 1 
        pointer = 0
        
        while pointer <= right:
            if nums[pointer] == 0:
                nums[pointer], nums[left] = nums[left], nums[pointer]
                left += 1 
                pointer += 1 
            elif nums[pointer] == 1:
                pointer += 1 
            else:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                right -= 1
