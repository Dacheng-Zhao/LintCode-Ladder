class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        left = 0
        right = len(heights) - 1 
        maxWater = 0
        leftMax = 0
        rightMax = 0
        
        while left < right:
            leftMax = max(leftMax, heights[left])
            rightMax = max(rightMax, heights[right])
            if leftMax < rightMax:
                left += 1 
                if leftMax - heights[left] > 0:
                    maxWater += leftMax - heights[left]
            else:
                right -= 1 
                if rightMax - heights[right] > 0:
                    maxWater += rightMax - heights[right]
        return maxWater
        
