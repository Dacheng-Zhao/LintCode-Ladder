class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
    #     if not nums:
    #         return [[]]
    #     self.res = []
    #     self.DFS(nums, 0)
    #     return self.res
        
    # def DFS(self, nums, index):
    #     if index == len(nums):
    #         if nums[:] not in self.res:
    #             return self.res.append(nums[:])
        
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
                if ([m] + p) not in l:
                    l.append([m] + p)
        return l


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.numsLen = len(nums)
        self.res = []
        nums.sort()
        self.DFS(nums, [])
        return self.res
    
    def DFS(self, remain, temp):
        if len(temp) == self.numsLen:
            self.res.append(temp[:])
            
        for i in range(len(remain)):
            if i != 0 and remain[i] == remain[i - 1]:
                continue
            remaining = remain[:i] + remain[i + 1:]
            temp.append(remain[i])
            self.DFS(remaining, temp[:])
            temp.pop()
        
        