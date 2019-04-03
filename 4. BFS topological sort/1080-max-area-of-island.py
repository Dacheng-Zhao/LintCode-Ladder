class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """
    def maxAreaOfIsland(self, grid):
        # Write your code here
        if not grid:
            return 0 
        
        row = len(grid)
        col = len(grid[0])
        self.area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.res = 0
                    self.DFS(grid, i, j)
        return self.area
        
    def DFS(self, grid, row, col):
        if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] != 1:
            return 
        grid[row][col] = 0
        self.res += 1 
        self.area = max(self.area, self.res)
        self.DFS(grid, row + 1, col)
        self.DFS(grid, row, col + 1)
        self.DFS(grid, row - 1, col)
        self.DFS(grid, row, col - 1)
        
