class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        # write your code here
        result = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i and nums[i - 1] == nums[i]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left <= right and nums[left] == nums[left - 1]:
                        left += 1
                    while left <= right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return result