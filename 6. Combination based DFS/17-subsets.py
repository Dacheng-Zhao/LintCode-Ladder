class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        self.res = []
        nums.sort()
        def DFS(nums, temp, index):
            self.res.append(temp[:])
            for i in range(index, len(nums)):
                temp.append(nums[i])
                DFS(nums, temp, i + 1)
                temp.pop()
        
        DFS(nums, [], 0)
        return self.res