class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return an integer
    """
    def repeatedStringMatch(self, A, B):
        # write your code here
        count = 1 
        originalA = A
        if B in A:
            return 1
        while len(A) < 2 * len(B):
            count += 1 
            A += originalA
            if B in A:
                return count
        return - 1
