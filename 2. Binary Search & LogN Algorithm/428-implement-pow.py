class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        index = abs(n)
        result = 1
        while index != 0:
            if index % 2 != 0:
                result *= x
            x *= x
            index //= 2
        if n < 0:
            return 1 / result
        else:
            return result

test = Solution()
print(test.myPow(8.84372, -5))