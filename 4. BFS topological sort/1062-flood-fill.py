class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """
    def floodFill(self, image, sr, sc, newColor):
        # Write your code here
        if not image:
            return None 
        self.DFS(image, sr, sc, newColor, image[sr][sc])
        return image
    
    def DFS(self, image, sr, sc, newColor, oldColor):
        image[sr][sc] = newColor
        if sr + 1 < len(image) and oldColor == image[sr + 1][sc]:
            self.DFS(image, sr + 1, sc, newColor, oldColor)
        if sc + 1 < len(image[0]) and oldColor == image[sr][sc + 1]:
            self.DFS(image, sr, sc + 1, newColor, oldColor)
        if sr - 1 >= 0 and oldColor == image[sr - 1][sc]:
            self.DFS(image, sr - 1, sc, newColor, oldColor)
        if sc - 1 >= 0 and oldColor == image[sr][sc - 1]:
            self.DFS(image, sr, sc - 1, newColor, oldColor)
        
