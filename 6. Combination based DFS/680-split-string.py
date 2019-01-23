class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        
        self.result = []
        return self.DFS(s)
        
    
    def DFS(self, s):
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
            
        result1 = self.DFS(s[1:])
        result2 = self.DFS(s[2:])
        result = []
        print(result1)
        for r1 in result1:
            result.append([s[0]] + r1)
            print('r1 is', r1)
        for r2 in result2:
            result.append([s[0:2]] + r2)
            
        return result
    
    # def splitString(self, s):
    #     if len(s) == 0:
    #         return [[]]
    #     if len(s) == 1:
    #         return [[s]]
    #     result1 = self.splitString(s[1:])
    #     result2 = self.splitString(s[2:])
    #     result = []
    #     for r1 in result1:
    #         result.append([s[0]] + r1)
    #     for r2 in result2:
    #         print(r2)
    #         result.append([s[:2]] + r2)
    #     return result