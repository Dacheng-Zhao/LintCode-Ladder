class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        if not s or len(s) < 2:
            return []
        
        res = []
        
        for i in range(len(s)):
            if i != 0 and s[i] == '+':
                if s[i - 1] == '+':
                    res.append(s[:i - 1] + '--' + s[i + 1:])
        return res
            