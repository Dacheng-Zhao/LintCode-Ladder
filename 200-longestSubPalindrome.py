class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if s == "": return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]  #2d array
        res = ""
        
        '''
        If the string s were 'babad', think this:
                            j
                        b a b a d             0 1 2 3 4
                     b  T                  0  T
                     a    T                1 <- T
                i    b  T   T          i   2  T   T
                     a    T   T            3    <-- T
                     d          T          4          so on.
                                            iterations go left. checks top right. Checking top right is like 
                                            saying if u got substring 'baab' and u check top right for 'aa'.
        '''
        for i in range(n):
            for j in range(i, -1, -1):
                # if they are equal and (the substring is length 2 or 1  or  the inner substring is also palindrom by looking up-right)
                if s[i] == s[j] and (i-j < 2 or dp[i-1][j+1]):
                    dp[i][j] = True 
                    
                # if earlier if statement were True, get longer result
                if dp[i][j] and (i + 1) - j  > len(res):
                    res = s[j:i+1]
        return res

test = Solution()
print(test.longestPalindrome('asdfabacabadfs'))