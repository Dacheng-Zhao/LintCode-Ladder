class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        # Write your code here
        if not flowerbed:
            return False
        
        if n == 0:
            return True 
        
        res = 0
        left = 1
        if flowerbed[0] == 0:
            flowerbed[0] = 1
            res = 1
        
        while left < len(flowerbed):
            if flowerbed[left - 1] == 0 and flowerbed[left] == 0:
                flowerbed[left] = 1 
                res += 1
            left += 1 
        return res >= n
        
        
