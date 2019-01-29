class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        self.key = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        self.res = []
        
        if not digits:
            return []
        self.DFS(digits, 0, '')
        return self.res
        
    def DFS(self, digits, index, comb):
        if index == len(digits):
            return self.res.append(comb)
        for i in self.key[digits[index]]:
            self.DFS(digits, index + 1, comb + i)
    
            