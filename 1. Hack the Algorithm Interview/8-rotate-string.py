class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if not str:
            return ''
            
        l = len(str)
        offset %= l 
        
        self.reverse(str, 0, l - offset - 1)
        self.reverse(str, l - offset, l - 1)
        self.reverse(str, 0, l - 1)
    
    def reverse(self, string, left, right):
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1 
            right -= 1 
        