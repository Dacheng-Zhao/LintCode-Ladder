class Solution:
    """
    @param s: a string
    @return: whether the student could be rewarded according to his attendance record
    """
    def checkRecord(self, s):
        # Write your code here
        if not s:
            return True 
        
        countA = 0 
        continueCountL = 0
        maxCountL = 0
        
        for i in range(len(s)):
            if s[i] == 'A':
                countA += 1 
            if i != 0 and s[i - 1] == s[i]:
                if s[i] == 'L':
                    if i - 2 >= 0 and s[i - 2] == 'L':
                        continueCountL += 1 
                    else:
                        continueCountL += 2
                    maxCountL = max(maxCountL, continueCountL)
            if s[i] != 'L':
                continueCountL = 0
        if countA > 1 or maxCountL > 2:
            return False
        return True
