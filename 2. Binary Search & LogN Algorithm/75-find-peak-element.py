class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if not A:
            return None

        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            else:
                start = mid

        if A[start] < A[end]:
            return end
        else:
            return start             

test = Solution()
print(test.findPeak([1,2,1,3,4,5,7,8])) 

        