class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return 0
        if target is None:
            return 0
        
        tempArray = []
        
        for i in range(len(matrix)):
            tempArray += matrix[i]
        self.quickSort(tempArray, 0, len(tempArray) - 1)
        print(tempArray)
        
        start = 0
        end = len(tempArray) - 1 
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if tempArray[mid] < target:
                start = mid
            else:
                end = mid
        
        if tempArray[start] == target:
            leftbound = start
        elif tempArray[end] == target:
            leftbound = end 
        else:
            return 0
            
        start = leftbound
        end = len(tempArray) - 1 
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if tempArray[mid] <= target:
                start = mid
            else:
                end = mid
        if tempArray[end] == target:
            rightbound = end 
        else:
            rightbound = start
        print(leftbound)
        print(rightbound)
        return rightbound - leftbound + 1
        
    
    def quickSort(self, A, start, end):
        if start >= end:
            return 
        left = start
        right = end
        mid = left + (right - left) // 2
        pivot = A[mid]
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


# from bottom left to top right corner
   if not matrix or not matrix[0]:
            return 0
        
        row = len(matrix)
        col = len(matrix[0])
        
        i = row - 1
        j = 0 
        count = 0
        
        while i >= 0 and j < col:
            if matrix[i][j] == target:
                count += 1 
                i -= 1 
                j += 1
            elif matrix[i][j] < target:
                j += 1 
            elif matrix[i][j] > target:
                i -= 1 
        return count
        
