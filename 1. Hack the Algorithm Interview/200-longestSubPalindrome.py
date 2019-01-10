class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    # dynamics programming
    def longestPalindrome(self, s):
        if not s:
            return ''
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ''
        
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1]):
                    dp[i][j] = True
                if dp[i][j] and (i + 1) - j > len(res):
                    res = s[j : i + 1]
        return res

    # central expand
    def longestPalindrome2(self, s):
        if not s:
            return ''
        
        n = len(s)
        res = ''

        for middle in range(n):
            sub = self.find_palindrome(s, middle, middle)
            if len(sub) > len(res):
                res = sub
            sub = self.find_palindrome(s, middle, middle + 1)
            if len(sub) > len(res):
                res = sub
        return res

    def find_palindrome(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1 : right]
test = Solution()
print(test.longestPalindrome2('ccc'))