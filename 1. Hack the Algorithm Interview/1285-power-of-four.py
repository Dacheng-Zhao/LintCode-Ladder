class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        # Write your code here
        # if not num or num < 0:
        #     return False
        
        # while num >= 1:
        #     if num == 1:
        #         return True 
        #     num /= 4
        # return False
        
        if not num or num < 0:
            return False
        
        if num & (num - 1) != 0:
            return False
        
        while num > 0:
            if num == 1:
                return True
            
            num >>= 2 
        
        return False
