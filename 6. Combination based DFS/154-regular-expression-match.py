class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, source, pattern):
        return self.is_match_helper(source, 0, pattern, 0, {})
        
        
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    # 能 return True
    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # source is empty
        if len(source) == i:
            return self.is_empty(pattern[j:])
            
        if len(pattern) == j:
            return False
            
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j + 2, memo)
        else:                
            matched = self.is_match_char(source[i], pattern[j]) and \
                self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        
        memo[(i, j)] = matched
        return matched
        
        
    def is_match_char(self, s, p):
        return s == p or p == '.'
        
    def is_empty(self, pattern):
        if len(pattern) % 2 == 1:
            return False
        
        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != '*':
                return False
        return True



# class Solution:
#     """
#     @param s: A string 
#     @param p: A string includes "?" and "*"
#     @return: is Match?
#     """
#     def isMatch(self, s, p):
#         matched = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
#         matched[0][0] = True
        
#         for i in range(len(s) + 1):
#             for j in range(1, len(p) + 1):
#                 pattern = p[j - 1]
                
#             if pattern == '.':
#                 matched[i][j] = (i != 0 and matched[i - 1][j - 1])
#             elif pattern == '*':
#                 star = p[j - 2]
#                 matched[i][j] = matched[i][j - 2] or (i > 0 and matched[i - 1][j] and (star == s[i - 1] or star =='.'))
                
#             else:
#                 matched[i][j] = (i != 0 and matched[i - 1][j - 1] and s[i - 1] == pattern)
        
#         return matched[-1][-1]
                
# class Solution:
#     """
#     @param s: A string 
#     @param p: A string includes "." and "*"
#     @return: A boolean
#     """
#     hash = None
#     def isMatch(self, s, p):
#         if self.hash is None:
#             self.hash = {}
#         key = s + p
#         if key in self.hash:
#             return self.hash[key]
            
#         if p == '':
#             return s == ''
#         if s == '':
#             if len(p) % 2 == 1:
#                 return False
#             i = 1
#             while i < len(p):
#                 if p[i] != '*':
#                     return False
#                 i += 2
#             return True
        
#         if len(p) > 1 and p[1] == '*':
#             if p[0] == '.':
#                 self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
#             elif p[0] == s[0]:
#                 self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
#             else:
#                 self.hash[key] = self.isMatch(s, p[2:])
#         elif p[0] == '.':
#             self.hash[key] = self.isMatch(s[1:], p[1:])
#         else:
#             self.hash[key] = s[0] == p[0] and self.isMatch(s[1:], p[1:])
        
#         return self.hash[key]

class Solution(object):
    # DP
    # def isMatch(self, s, p):
    #     dp = [[False for i in range(0,len(p) + 1)] for j in range(0, len(s) + 1)]
    #     dp[0][0] = True
    #     for i in range(1, len(p) + 1):
    #         if (p[i - 1] == '*'):
    #             dp[0][i] = dp[0][i - 2]
    #     for i in range(1, len(s) + 1):
    #         for j in range(1, len(p) + 1):
    #             if p[j - 1] == '*':
    #                 dp[i][j] = dp[i][j - 2]
    #                 if s[i - 1] == p[j - 2] or p[j - 2] == '.':
    #                     dp[i][j] |= dp[i-1][j]
    #             else:
    #                 if s[i - 1] == p[j - 1] or p[j - 1] == '.':
    #                     dp[i][j] = dp[i - 1][j - 1]
    
    #     return dp[len(s)][len(p)]

    # # 懒癌版
    def isMatch(self, s, p):
        return re.match(p + '$', s) != None