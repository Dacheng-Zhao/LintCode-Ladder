class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        if not matrix:
            return []
        
        zeroRow = []
        zeroCol = []
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i not in zeroRow:
                        zeroRow.append(i)
                    if j not in zeroCol:
                        zeroCol.append(j)
        
        while zeroRow:
            removeRow = zeroRow.pop()
            for i in range(col):
                matrix[removeRow][i] = 0

        while zeroCol:
            removeCol = zeroCol.pop()
            for i in range(row):
                matrix[i][removeCol] = 0
        
        return matrix
                    
        