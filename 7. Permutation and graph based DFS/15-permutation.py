class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
    #     if not nums:
    #         return [[]]
    #     self.res = []
    #     self.DFS(nums, 0)
    #     return self.res
    
    # def DFS(self, nums, index):
    #     if index == len(nums):
    #         return self.res.append(nums[:])
        
    #     for i in range(index, len(nums)):
    #         nums[i], nums[index] = nums[index], nums[i]
    #         self.DFS(nums, index + 1)
    #         nums[i], nums[index] = nums[index], nums[i]
    
        if not nums:
            return [[]]
        
        return self.DFS(nums)
    
    
    def DFS(self, nums):
        if len(nums) == 0:
            return []
            
        if len(nums) == 1:
            return [nums]
            
        l = []
        
        for i in range(len(nums)):
            m = nums[i]
            
            remain = nums[:i] + nums[i+1:]
            
            for p in self.DFS(remain):
                l.append([m] + p)
        return l

        