class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    # [5,6,0,1,2,3,4]
    # [0,1,2,3,4,5,6]
    # [2,3,4,5,6,0,1]
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        
        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return mid
            
            if A[start] <= A[mid]: # left hand side sorted
                if target >= A[start] and target < A[mid]:
                    end = mid
                else:
                    start = mid
            else:  # right hand side sorted
                if target <= A[end] and target > A[mid]:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1

test = Solution()
print(test.search([3,4,5,0,1,2], 3))
print(test.search([3,4,5,0,1,2], 2))
