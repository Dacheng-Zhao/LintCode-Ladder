class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        dictres = {0 : -1}
        subsum = 0
        
        for i, num in enumerate(nums):
            subsum += num
            if subsum in dictres:
                return dictres[subsum] + 1, i
            dictres[subsum] = i
        return -1, -1