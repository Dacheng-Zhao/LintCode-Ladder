class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        if not S or len(S) < 3:
            return 0
        self.quickSort(S, 0, len(S) - 1)
        count = 0
        for i in range(len(S) - 1, -1, -1):
            thirdLargest = S[i]
            left = 0
            right = i - 1
            while left < right:
                if S[left] + S[right] > thirdLargest:
                    count += right - left
                    right -= 1
                else:
                    left += 1 
        return count
        
    
    def quickSort(self, A, start, end):
        if start >= end:
            return
        
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
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
