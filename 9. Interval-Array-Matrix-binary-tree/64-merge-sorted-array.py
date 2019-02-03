class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        # for i in range(n):
        #     A[m + i] = B[i]
        # return A.sort()
        
        i = m - 1 
        j = n - 1 
        end = m + n - 1 
        
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[end] = A[i]
                i -= 1 
                end -= 1 
            else:
                A[end] = B[j]
                j -= 1 
                end -= 1 
        while j >= 0:
           A[end] = B[j]
           end -= 1 
           j -= 1
