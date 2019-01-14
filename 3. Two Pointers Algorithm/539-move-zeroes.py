class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
         # [1,0,2,0,3,4,5]
        # slow = 0
        # keep slow at zero
        # for fast, num in enumerate(nums):
        #     if num != 0:
        #         if slow < fast:
        #             nums[slow] = num
        #             nums[fast] = 0
        #         slow += 1

        if not nums:
            return None
        i,j = 0, 0
        while i + j < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                j += 1
            else:
                i += 1