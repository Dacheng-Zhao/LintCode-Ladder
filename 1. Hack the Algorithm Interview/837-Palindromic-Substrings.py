class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, str):
        # write your code here
        # if not str:
        #     return 0
        
        # n = len(str)
        # dp = [[0] * n for _ in range(n)]
        # res = 0
        
        # for i in range(n):
        #     for j in range(i, -1, -1):
        #         if str[i] == str[j] and (i - j < 2 or dp[i - 1][j + 1] == 1):
        #             dp[i][j] = 1 
        #             res += 1 
        # return res 
        if not str:
            return 0
        
        n = len(str)
        self.res = 0
        
        for middle in range(n):
            self.findPalindrome(str, middle, middle)
            self.findPalindrome(str, middle, middle + 1)
        
        return self.res
        
    def findPalindrome(self, str, left, right):
        while left >= 0 and right < len(str) and str[left] == str[right]:
            self.res += 1 
            left -= 1 
            right += 1 
        
