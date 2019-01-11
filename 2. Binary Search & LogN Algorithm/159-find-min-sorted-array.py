class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return None

        start = 0
        end = len(nums) - 1
        target = nums[end]

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])
        
test = Solution()
print(test.findMin([1,2,3,4,5,6]))
print(test.findMin([3,4,5,6,7,0,1,2]))