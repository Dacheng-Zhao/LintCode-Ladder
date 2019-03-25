class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
    #     if not n:
    #         return []
        
    #     partials = [[]]
        
    #     for col in range(n):
    #         new_partials = []
    #         for partial in partials:
    #             for row in range(n):
    #                 if not self.conflict(partial, row):
    #                     print(partial)
    #                     print(row)
    #                     new_partials.append(partial + [row])
    #                     print(new_partials)
    #         partials = new_partials
        
    #     results = []
    #     for partial in partials:                # convert result to strings
    #         result = [['.'] * n for _ in range(n)]
    #         for col, row in enumerate(partial):
    #             result[row][col] = 'Q'
    #         for row in range(n):
    #             result[row] = ''.join(result[row])
    #         results.append(result)

    #     return results

    # def conflict(self, partial, new_row):
    #     for col, row in enumerate(partial):
    #         if new_row == row:                      # same row
    #             return True
    #         col_diff = len(partial) - col
    #         if abs(new_row - row) == col_diff:      # same diagonal
    #             return True

    #     return False
    
        results = []
        self.search(n, [], results)
        return results
        
    def search(self, n, cols, results):
        row = len(cols)
        if row == n:
            results.append(self.draw_chessboard(cols))
            return

        for col in range(n):
            if not self.is_valid(cols, row, col):
                continue
            cols.append(col)
            self.search(n, cols, results)
            cols.pop()
            
    def draw_chessboard(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
        
    def is_valid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r - c == row - col or r + c == row + col:
                return False
        return True
        
        
            
