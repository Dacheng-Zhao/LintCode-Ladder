class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    # brutal force
    def lastPosition(self, nums, target):
        if not nums:
            return -1

        for i in range(len(nums) -1, -1, -1):
            if nums[i] == target:
                return i
        return -1

    # binary search
    def lastPosition2(self, nums, target):
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            # prevent out of index
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid 
            else:
                # combine <= and move
                start = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1

test = Solution()
print(test.lastPosition2([1,2,2,2,2,3,4,5], 2))