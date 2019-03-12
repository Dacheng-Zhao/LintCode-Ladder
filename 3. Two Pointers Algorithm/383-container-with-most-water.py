class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        # write your code here
        if not heights or len(heights) == 1:
            return 0
        mostWater = 0
        left = 0
        right = len(heights) - 1 
        
        while left < right:
            while left < right and heights[left] <= heights[right]:
                mostWater = max(mostWater, heights[left] * (right - left))
                left += 1 
            while left < right and heights[left] >= heights[right]:
                mostWater = max(mostWater, heights[right] * (right - left))
                right -= 1 
        return mostWater
