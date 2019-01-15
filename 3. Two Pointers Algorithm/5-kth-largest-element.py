class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums:
            return None
        if n > len(nums):
            return None
        
        return self.quickSort(0, len(nums) - 1, nums, len(nums) - n)
        
    def quickSort(self, start, end, A, k):
        if start >= end:
            return A[k]
        left = start
        right = end
        pivot = A[start + (end - start) // 2]
        
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1 
            while left <= right and A[right] > pivot:
                right -= 1 
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1 
                right -= 1 
        if k <= right:
            return self.quickSort(start, right, A, k)
        if k >= left:
            return self.quickSort(left, end, A, k)
        return A[k]
                