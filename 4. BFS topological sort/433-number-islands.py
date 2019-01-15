import collections

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    # def numIslands(self, grid):
    #     # write your code here
    #     if not grid or not grid[0]:
    #         return 0
        
    #     n = len(grid)
    #     m = len(grid[0])
    #     islands = 0
        
    #     for i in range(n):
    #         for j in range(m):
    #             if grid[i][j] == 1:
    #                 islands += 1 
    #                 self.dfs(grid, i, j, n, m)
    #     return islands
        
    
    # def dfs(self, grid, i, j, n, m):
    #     if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
    #         return
    #     grid[i][j] = 0
        
    #     self.dfs(grid, i + 1, j, n, m)
    #     self.dfs(grid, i, j + 1, n, m)
    #     self.dfs(grid, i - 1, j, n, m)
    #     self.dfs(grid, i, j - 1, n, m)
    
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        n = len(grid)
        m = len(grid[0])
        islands = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    islands +=  1 
                    self.bfs(grid, i, j, n, m)
        return islands
        
    def bfs(self, grid, i, j, n, m):
        if i < 0 or j < 0 or i >= n or j >=m:
            return
        queue = collections.deque()
        queue.append((i, j))
        grid[i][j] = 0
        while queue:
            i, j = queue.popleft()
            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            for d in directions:
                a, b = i + d[0], j + d[1]
                if not (a < 0 or b < 0 or a >= n or b >= m) and grid[a][b] == 1:
                    queue.append((a, b))
                    grid[a][b] = 0
            
        