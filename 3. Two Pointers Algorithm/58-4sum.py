class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 4:
            return []
        numbers.sort()
        res = []
        
        for i in range(len(numbers) - 3):
            if i != 0 and numbers[i] == numbers[i - 1]:
                continue
            else:
                for j in range(i + 1, len(numbers) - 2):
                    if j != i + 1 and numbers[j] == numbers[j - 1]:
                        continue
                    left = j + 1 
                    right = len(numbers) - 1 
                    while left < right:
                        if (numbers[i] + numbers[j] + numbers[left] + numbers[right]) == target:
                            res.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                            left += 1 
                            right -= 1 
                            while left < right and numbers[left] == numbers[left - 1]:
                                left += 1 
                            while left < right and numbers[right] == numbers[right + 1]:
                                right -= 1 
                        elif (numbers[i] + numbers[j] + numbers[left] + numbers[right]) > target:
                            right -= 1 
                        else:
                            left += 1 
        return res
