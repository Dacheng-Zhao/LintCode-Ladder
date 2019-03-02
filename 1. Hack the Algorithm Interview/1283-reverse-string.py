class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        # write your code here
        if not s:
            return ''
        
        res = []
        
        # for ele in s[::-1]:
        #     res.append(ele)
        
        for i in range(len(s) - 1, -1, -1):
            res.append(s[i])
        
        res = ''.join(res)
        return res
