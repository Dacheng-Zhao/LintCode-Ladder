class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.quickSort(0, len(colors) - 1, colors)
        
    def quickSort(self, start, end, colors):
        if start >= end:
            return
        pivot = colors[start + (end - start) // 2]
        left = start
        right = end
        
        while left <= right:
            while left <= right and colors[left] < pivot:
                left += 1 
            while left <= right and colors[right] > pivot:
                right -= 1 
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1 
                right -= 1
        self.quickSort(start, right, colors)
        self.quickSort(left, end, colors)
        