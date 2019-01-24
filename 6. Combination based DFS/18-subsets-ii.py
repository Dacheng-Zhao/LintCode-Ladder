class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        self.res = []
        temp = []
        nums.sort()
        
        def DFS(nums, temp, index):
            self.res.append(temp[:])
            last_num = None
            for i in range(index, len(nums)):
                if last_num is not None and nums[i] == last_num:
                    continue
                temp.append(nums[i])
                DFS(nums, temp, i + 1)
                last_num = temp.pop()
                temp.pop
                
            
        
        DFS(nums, [], 0)
        return self.res


   self.res = []
        temp = []
        nums.sort()
        
        def DFS(nums, temp, index):
            self.res.append(temp[:])
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                DFS(nums, temp, i + 1)
                temp.pop()
                
        DFS(nums, [], 0)
        return self.res