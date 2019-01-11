class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        # (a * b) % p = ((a % p) * (b % p)) % p
        # if n == 1:
        #     return a % b
        # elif n == 0:
        #     return 1 % b
        # elif n < 0:
        #     return -1
        # init = a
        # while n > 0 and n != 1:
        #     # a *= a
        #     a = a * a % b
        #     n //= 2
        # else:
        #     if n == 1:
        #         return ((a % b) * (init % b)) % b
        #     else:
        #         return a % b 
        # exceed limit

        # (a * a^2 * a^4 * a^8) % p = ...
        ans = 1
        while n > 0:
            if n % 2==1:
                ans = ans * a % b
            a = a * a % b
            n = n // 2
        return ans % b


test = Solution()
print(test.fastPower(2, 3, 30))