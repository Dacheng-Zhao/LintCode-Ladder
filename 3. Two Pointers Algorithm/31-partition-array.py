class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0

        self.quickSort(0, len(nums) - 1, nums)
        
        if k < nums[0]:
            return 0
        elif k > nums[len(nums) - 1]:
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] == k:
                return i
        
        
    def quickSort(self, start, end, A):
        if start >= end:
            return
        left = start
        right = end
        pivot = A[start + (end - start) // 2]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1 
        self.quickSort(start, right, A)
        self.quickSort(left, end, A)

test = Solution()
# print(test.partitionArray([7,7,9,8,6,6,8,7,9,8,6,6], 10))
print(test.partitionArray([3,2,1], 2))