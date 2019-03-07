class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not target:
            return False
        tempArray = []
        for i in range(len(matrix)):
            tempArray += matrix[i]
        
        start = 0
        end = len(tempArray) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if tempArray[mid] > target:
                end = mid
            else:
                start = mid
        
        if tempArray[start] == target or tempArray[end] == target:
            return True
        return False
