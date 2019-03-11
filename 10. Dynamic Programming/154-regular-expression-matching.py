class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        lenS = len(s) + 1 
        lenP = len(p) + 1 
        dp = [[False] * lenP for _ in range(lenS)]
        dp[0][0] = True
        
        for i in range(1, lenP):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        
        for i in range(1, lenS):
            for j in range(1, lenP):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] != s[i - 1] and p[j - 2] != '.':
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i][j - 2]
        return dp[lenS - 1][lenP - 1]
