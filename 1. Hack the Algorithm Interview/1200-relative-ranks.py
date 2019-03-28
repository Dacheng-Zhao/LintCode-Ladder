class Solution:
    """
    @param nums: List[int]
    @return: return List[str]
    """
    def findRelativeRanks(self, nums):
        # write your code here
        if not nums:
            return []
        dummy = nums[:]
        nums.sort()
        nums.reverse()
        rankDict = {}

        for i in range(len(nums)):
            rankDict[nums[i]] = str(i + 1)
        
        for key, val in rankDict.items():
            if val >= '4':
                break
            if val == '1':
                rankDict[key] = "Gold Medal"
            if val == '2':
                rankDict[key] = "Silver Medal"
            if val == '3':
                rankDict[key] = "Bronze Medal"

        for j in range(len(dummy)):
            dummy[j] = rankDict[dummy[j]]
        
        return dummy
            
        
        