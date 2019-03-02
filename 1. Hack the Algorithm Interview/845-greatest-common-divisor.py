class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        if not a or not b:
            return None 
        
        smaller = min(a, b)
        
        for i in range(smaller, 1, -1):
            if a % i == 0 and b % i == 0:
                return i 
        return 1

# there is an algorithm for it, need math