class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        # write your code here
        if not matrix:
            return []
        
        n = len(matrix)
        
        top = 0
        left = 0
        right = n - 1 
        bottom = n - 1
        
        while n > 1:
            for i in range(n - 1):
                temp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = temp
            top += 1
            left += 1 
            right -= 1 
            bottom -= 1 
            n -= 2

    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse() 
            
            
        