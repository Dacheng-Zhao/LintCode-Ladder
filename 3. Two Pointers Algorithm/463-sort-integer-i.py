class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        # bubbule sort
        # for i in range(len(A), -1, -1):
        #     for j in range(1, i):
        #         if A[j - 1] > A[j]:
        #             temp = A[j - 1]
        #             A[j - 1] = A[j]
        #             A[j] = temp
        
        # selection sort
        # for i in range(len(A) - 1, -1, -1):
        #     biggest = A[0]
        #     biggestIndex = 0
        #     for j in range(1, i + 1):
        #         if A[j] > biggest:
        #             biggest = A[j]
        #             biggestIndex = j
        #     temp = A[i]
        #     A[i] = biggest
        #     A[biggestIndex] = temp
                    
        # insertion sort
        for i in range(1, len(A)):
            comparedValue = A[i]
            j = i - 1 
            
            while j >= 0 and A[j] > comparedValue:
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = comparedValue