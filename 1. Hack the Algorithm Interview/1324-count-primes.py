class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        # write your code here
        if n < 3:
            return 0 
        
        prime = [True for _ in range(n)]
        prime[0] = False
        prime[1] = False
        prime[2] = True
        
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
        return sum(prime)
