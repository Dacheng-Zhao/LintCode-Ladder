class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        if not matrix:
            return True 
        
        topLine = 0
        leftLine = 0
        
        for i in range(len(matrix)):
            topLine = i
            while topLine < len(matrix) and leftLine < len(matrix[0]):
                if topLine != 0 and leftLine != 0:
                    if matrix[topLine][leftLine] != matrix[topLine - 1][leftLine - 1]:
                        return False
                topLine += 1 
                leftLine += 1 
        return True
        
