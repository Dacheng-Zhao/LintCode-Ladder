class Solution:
    """
    @param A: string A
    @param B: string B
    @return: bool
    """
    def buddyStrings(self, A, B):
        # Write your code here
        if not A and not B:
            return True

        if len(A) != len(B):
            return False
        
        if A == B and len(set(A)) < len(A):
            return True

        left = -1
        right = -1
        count = 0
        
        for i in range(len(A)):
            if A[i] != B[i]:
                if left == -1:
                    left = i
                elif right == -1:
                    right = i 
                count += 1 

        if count > 2 or count == 1:
            return False
        
        if count == 2 and A[left] == B[right] and A[right] == B[left]:
            return True
        else:
            return False
