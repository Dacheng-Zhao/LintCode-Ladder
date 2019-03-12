class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        # write your code here
        if not s or len(s) == 0:
            return 0
        
        numSum = 0
        for ele in s:
            if ele == 'M':
                numSum += 1000
            elif ele == 'D':
                numSum += 500
            elif ele == 'C':
                numSum += 100
            elif ele == 'L':
                numSum += 50
            elif ele == 'X':
                numSum += 10
            elif ele == 'V':
                numSum += 5
            elif ele == 'I':
                numSum += 1
        
        if 'CD' in s:
            numSum -= 200
        if 'CM' in s:
            numSum -= 200
        if 'XL' in s:
            numSum -= 20
        if 'XC' in s:
            numSum -= 20
        if 'IV' in s:
            numSum -= 2
        if 'IX' in s:
            numSum -= 2
        
        return numSum
