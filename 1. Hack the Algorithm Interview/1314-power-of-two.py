class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):
        # Write your code here
        if not n or n < 0:
            return False 
        
        x = 0
        
        while x < 32:
            if 1 << x == n:
                return True 
            x += 1 
        return False
    
