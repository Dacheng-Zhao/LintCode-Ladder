class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        if not moves:
            return True 
        
        xAxis = 0
        yAxis = 0
        
        for char in moves:
            if char == 'U':
                yAxis += 1 
            elif char == 'D':
                yAxis -= 1 
            elif char == 'L':
                xAxis -= 1 
            elif char == 'R':
                xAxis += 1 
        return xAxis == 0 and yAxis == 0
