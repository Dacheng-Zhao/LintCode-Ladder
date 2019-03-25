class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        if not n:
            return []
        self.results = 0
        self.search(n, [])
        return self.results
        
    def search(self, n, cols):
        row = len(cols)
        if row == n:
            self.results += 1 
            return 
        
        for col in range(n):
            if not self.is_valid(cols, col, row):
                continue
            cols.append(col)
            self.search(n, cols)
            cols.pop()
            
    def is_valid(self, cols, col, row):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if abs(col - c) == row - r:
                return False
        return True
        
        
