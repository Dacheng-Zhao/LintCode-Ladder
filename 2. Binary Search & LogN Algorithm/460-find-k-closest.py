class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A or k > len(A) or k <= 0:
            return []
        
        start = 0
        end = len(A) - 1
        result = []

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] > target:
                end = mid
            else:
                start = mid
        if A[start] == target:
            target_index = start
        if A[end] == target:
            target_index = end
        
        while len(result) < k:
            left_diff = abs(A[start] - target) if start >=0 else None
            right_diff = abs(A[end] - target) if end < len(A) else None

            if left_diff != None and right_diff != None:
                if right_diff < left_diff:
                    result.append(A[end])
                    end += 1
                else:
                    result.append(A[start])
                    start -= 1
            elif left_diff != None:
                result.append(A[start])
                start -= 1
            elif right_diff != None:
                result.append(A[end])
                end += 1
            else:
                break
        return result



test = Solution()
print(test.kClosestNumbers([1, 4, 6, 8], 3, 3))
        