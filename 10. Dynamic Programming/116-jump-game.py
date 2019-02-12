class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        # maxstep = 0
        # for i in range(len(A)):
        #     if i > maxstep:
        #         return False
        #     maxstep = max(maxstep, i + A[i])
        # return True
        
        l = len(A)
        dp = [1] + [0] * (l-1)
        for i in range(l):
            if dp[i] == 0:
                continue
            for j in range(A[i]):
                if i + j + 1 < l:
                    dp[i+j+1] = 1 
        return dp[-1] == 1
        
        
        