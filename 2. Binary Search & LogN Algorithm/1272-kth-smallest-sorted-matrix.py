class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        # if not matrix or k > len(matrix) ** 2:
        #     return None 
        
        # n = len(matrix)
        # newArray = []
        
        # for i in range(n):
        #     newArray += matrix[i]
        
        # newArray.sort()
        
        # return newArray[k - 1]
        
        # binary search
        
        row = len(matrix) - 1
        col = len(matrix) - 1
        minNum = matrix[0][0]
        maxNum = matrix[row][col]
        start = minNum
        end = maxNum
        
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if self.countNumbers(matrix, mid, row, col) < k:
                start = mid 
            else:
                end = mid 
        if self.countNumbers(matrix, start, row, col) >= k:
            return start
        return end 
            
            
    def countNumbers(self, matrix, mid, row, col):
        count = 0
        i = 0
        j = col 
        while i <= row and j >= 0:
            if matrix[i][j] <= mid:
                i += 1 
                count += j + 1 
            else:
                j -= 1 
        return count
        