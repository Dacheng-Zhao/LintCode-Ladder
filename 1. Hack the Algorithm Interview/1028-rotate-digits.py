class Solution:
    """
    @param N: a positive number
    @return: how many numbers X from 1 to N are good
    """
    def rotatedDigits(self, N):
        # write your code here
        
        res = 0
        for i in range(N + 1):
            newStr = str(i)
            if '3' in newStr or '4' in newStr or '7' in newStr:
                continue
            if '2' in newStr or '5' in newStr or '6' in newStr or '9' in newStr:
                res += 1 
        return res