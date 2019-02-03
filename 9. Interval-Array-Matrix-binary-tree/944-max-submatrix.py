class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code here
        
        
        if not matrix or not matrix[0]:
            return 0 
            
        maxSum = -sys.maxsize
        rows, columns = len(matrix), len(matrix[0])
        for topRow in range(rows):
            compressedRow = [0] * columns 
            for row in range(topRow, rows):
                minSum, nextPrefixSum = 0, 0 
                for col in range(columns):
                    compressedRow[col] += matrix[row][col]
                    nextPrefixSum += compressedRow[col]
                    print(compressedRow)
                    maxSum = max(maxSum, nextPrefixSum - minSum)
                    print(maxSum)
                    minSum = min(minSum, nextPrefixSum)
        
        return maxSum
        
    # def maxSubmatrix(self, matrix):
    #     if len(matrix) == 0: return 0
    #     if len(matrix[0]) == 0: return 0
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     prefixSumCol = self.getPrefixSumCol(matrix)
    #     max_value = -sys.maxsize - 1 
    #     for up in range(row):
    #         for down in range(up, row):
    #             array = self.compression(matrix, up, down, prefixSumCol)
    #             max_value = max(max_value, self.maxSubArray(array))
    #     return max_value
    
    # def maxSubArray(self, array):
    #     min_value = 0;
    #     max_value = -sys.maxsize - 1 
    #     sum = 0 
    #     for arr in array:
    #         sum += arr
    #         max_value = max(max_value, sum - min_value)
    #         min_value = min(min_value, sum)
    #     return max_value


    # def compression(self, matrix, up, down, prefixSumCol):
    #     col = len(matrix[0])
    #     array = [0 for i in range(col)]
    #     for i in range(col):
    #         array[i] = prefixSumCol[down+1][i] - prefixSumCol[up][i] 
    #     return array 

    # def getPrefixSumCol(self, matrix):
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     prefixSumCol = [[0 for i in range(col)] for j in range(row+1)]
    #     for i in range(row):
    #         for j in range(col):
    #             prefixSumCol[i+1][j] = prefixSumCol[i][j] + matrix[i][j]
    #     return prefixSumCol
    
        
        
              
              
               
            
        