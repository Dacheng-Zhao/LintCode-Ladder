class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        # if not A or not B:
        #     return []
            
        # a = len(A)
        # b = len(B)
        # c = len(B[0])
        
        # M = [[0]*c for _ in range(a)]
        
        # for i in range(a):
        #     for j in range(c):
        #         for k in range(b):
        #             M[i][j] += A[i][k] * B[k][j]
        # return M
        
        if not A or not B:
            return []
            
        a = len(A)
        b = len(A[0])
        c = len(B[0])
        
        M = [[0] * c for _ in range(a)]
        
        for i in range(a):
            for j in range(b):
                if A[i][j] != 0:
                    for k in range(c):
                        M[i][k] += A[i][j] * B[j][k]
        return M