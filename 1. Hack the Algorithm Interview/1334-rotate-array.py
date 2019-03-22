class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums, k):
        # Write your code here
        if not nums:
            return []
        
        n = len(nums)
        k %= n 
        
        return nums[n - k :] + nums[: n - k]
