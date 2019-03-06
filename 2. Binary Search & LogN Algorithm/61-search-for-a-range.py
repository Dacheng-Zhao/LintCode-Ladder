class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A or not target:
            return [-1, -1]
            
        start = 0
        end = len(A) - 1 
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        
        if A[start] == target:
            leftbound = start
        elif A[end] == target:
            leftbound = end
        else:
            return [-1, -1]
        
        start = leftbound
        end = len(A) - 1 
        
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if A[mid] <= target:
                start = mid
            else:
                end = mid 
                
        if A[end] == target:
            rightbound = end 
        else:
            rightbound = start
            
        return [leftbound, rightbound]
        