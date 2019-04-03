class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):
        # Write your code here
        # find prime array from 0 - 32
        primeArray = [True for _ in range(32)]
        primeArray[0] = False 
        primeArray[1] = False
        for i in range(32):
            if primeArray[i]:
                for j in range(i * i, 32, i):
                    primeArray[j] = False 
        res = 0
        
        for t in range(L, R + 1):
            count = 0
            while t > 0:
                count += t & 1 
                t = t >> 1 
            if primeArray[count]:
                res += 1 
        return res 
        
