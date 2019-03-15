class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 3:
            return None 
        numbers.sort()
        compare = sys.maxsize
        
        for i in range(len(numbers) - 2):
            left = i + 1
            right = len(numbers) - 1 
            
            while left < right:
                diff = numbers[i] + numbers[left] + numbers[right] - target
                if diff == 0:
                    return target
                if abs(compare) > abs(diff):
                    compare = diff
                if diff > 0:
                    right -= 1
                else:
                    left += 1 
        return target + compare
        
