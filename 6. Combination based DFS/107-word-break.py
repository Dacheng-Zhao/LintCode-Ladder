class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        # not working
        # self.res = []
        # temp = ''
        # dicts = list(dict)
        # if not s:
        #     return True
        # if dicts == []:
        #     return False
        
        # def DFS(s, resstring, index):
        #     self.res.append(resstring)
        #     resstring = ''
        #     for i in range(index, len(s)):
        #         resstring += s[i]
        #         DFS(s, resstring, i + 1)
                
        # DFS(s, temp, 0)
        # print(self.res)
        # for j in range(len(dict)):
        #     if dicts[j] not in self.res:
        #         return False
        
        # return True
        
        if len(dict) == 0:
            return len(s) == 0
        
        can_make = [False] * (len(s) + 1)
        can_make[0] = True
        maxLength = max([len(w) for w in dict])
        
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if i - j > maxLength:
                    break
                if can_make[j] and s[j:i] in dict:
                    can_make[i] = True
                    break
        return can_make[-1]
        
        # if len(dict) == 0:
        #     return len(s) == 0
            
        # n = len(s)
        # f = [False] * (n + 1)
        # f[0] = True
        
        # maxLength = max([len(w) for w in dict])
        # for i in range(1, n + 1):
        #     for j in range(1, min(i, maxLength) + 1):
        #         if not f[i - j]:
        #             continue
        #         if s[i - j:i] in dict:
        #             f[i] = True
        #             break
        
        # return f[n]