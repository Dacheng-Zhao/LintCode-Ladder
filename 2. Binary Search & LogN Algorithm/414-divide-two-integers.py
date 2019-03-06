class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        if dividend == 0:
            return 0
        
        neg = False
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            neg = True
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        shift = 31
        
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1 
        
        if neg:
            ans = -ans
        
        if ans > INT_MAX:
            return INT_MAX
        
        return ans
        
