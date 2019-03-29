class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    def kthPrime(self, n):
        # write your code here
        # primeArray = [2]
        # step = 1
        # while primeArray[-1] < n:
        #     start = primeArray[-1] + step
        #     isPrime = True
        #     for i in range(2, start):
        #         if start % i == 0:
        #             isPrime = False
        #             step += 1
        #             break
        #     if isPrime:
        #         step = 1
        #         primeArray.append(start)
        
        # return len(primeArray)
        if n < 2:
            return 0
            
        if n == 2:
            return 1 
        
        prime = [True for _ in range(n + 1)]
        prime[0] = False
        prime[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    prime[j] = False
        return sum(prime)
                
        