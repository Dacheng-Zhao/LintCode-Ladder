class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        charDict = {}
        for c in str:
            if c not in charDict:
                charDict[c] = 1 
            else:
                charDict[c] += 1 
        for c in str:
            if charDict[c] == 1:
                return c 
        return None
