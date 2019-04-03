class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def findShortestSubArray(self, nums):
        # write your code here
        if not nums:
            return 0 
        
        degree = 0
        maxDegreeNumCollection = []
        numMap = {}
        res = sys.maxsize
        
        for i in range(len(nums)):
            if nums[i] not in numMap:
                numMap[nums[i]] = 1 
            else:
                numMap[nums[i]] += 1 
        
        for key, val in numMap.items():
            degree = max(degree, val)
        
        for key, val in numMap.items():
            if val == degree:
                maxDegreeNumCollection.append(key)
        
        for i in range(len(maxDegreeNumCollection)):
            left = 0
            right = len(nums) - 1
            while nums[left] != maxDegreeNumCollection[i]:
                left += 1 
            while nums[right] != maxDegreeNumCollection[i]:
                right -= 1 
            res = min(res, right - left + 1)
        return res 
            
                
            