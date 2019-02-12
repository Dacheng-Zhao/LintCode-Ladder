class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        
        if not A or len(A) == 1:
            return 0
        
        if A[0] > len(A) - 1:
            return 1
        
        currmaxjump = A[0]
        nextmaxjump = A[0]
        step = 1 
        index = 0 
        
        while nextmaxjump < len(A) - 1:
            while index <= nextmaxjump:
                currmaxjump = max(currmaxjump, index+A[index])
                index += 1
            step += 1 
            nextmaxjump = currmaxjump
        return step
        
