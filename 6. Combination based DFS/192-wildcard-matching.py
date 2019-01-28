class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        
        # i, j = 0, 0
        # star = -1
        # star_i = -1
        
        # while i < len(s):
        #     if j >= len(p) or (s[i] != p[j] and p[j] not in {"*", "?"}):
        #         if star == -1:
        #             return False
        #         j = star + 1 
        #         i += 1
                
        #     elif p[j] == '*':
        #         star = j 
        #         star_i = i
        #         j += 1
                
        #     else:
        #         i += 1 
        #         j += 1
                
        # while j < len(p):
        #     if p[j] != '*':
        #         return False
        #     j += 1 
        # return True
        
    #     return self.is_match_helper(s, 0, p, 0, {})
        
    # def is_match_helper(self, source, i, pattern, j, memo):
    #     if (i, j) in memo:
    #         return memo[(i, j)]
            
    #     # source is empty
    #     if len(source) == i:
    #         # every character should be "*"
    #         for index in range(j, len(pattern)):
    #             if pattern[index] != '*':
    #                 return False
    #         return True
            
    #     if len(pattern) == j:
    #         return False
            
    #     if pattern[j] != '*':
    #         matched = self.is_match_char(source[i], pattern[j]) and \
    #             self.is_match_helper(source, i + 1, pattern, j + 1, memo)
    #     else:                
    #         matched = self.is_match_helper(source, i + 1, pattern, j, memo) or \
    #             self.is_match_helper(source, i, pattern, j + 1, memo)
        
    #     memo[(i, j)] = matched
    #     return matched
        
        
    # def is_match_char(self, s, p):
    #     return s == p or p == '?'
    

        n = len(s)
        m = len(p)
        f = [[False] * (m + 1) for i in range(n + 1)]
        f[0][0] = True

        if n == 0 and p.count('*') == m:
            return True

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i > 0 and j > 0:
                    f[i][j] |= f[i-1][j-1] and (s[i-1] == p[j-1] or p[j - 1] in ['?', '*'])

                if i > 0 and j > 0:
                    f[i][j] |= f[i - 1][j] and p[j - 1] == '*'

                if j > 0:
                    f[i][j] |= f[i][j - 1] and p[j - 1] == '*'


        return f[n][m]