class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if not nums:
            return None

        for slow in range(len(nums) - 1):
            for fast in range(slow + 1, len(nums)):
                if nums[slow] + nums[fast] == target:
                    return [slow + 1, fast + 1]
                elif nums[slow] + nums[fast] < target:
                    continue
                else:
                    break
        return None

