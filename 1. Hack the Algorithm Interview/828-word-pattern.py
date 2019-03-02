class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        if not pattern or not teststr:
            return False 
        
        testarr = teststr.split(' ')
        hashMapA = {}
        
        flag = 1
        for i in range(len(pattern)):
            if pattern[i] not in hashMapA:
                hashMapA[pattern[i]] = testarr[i]
            elif hashMapA[pattern[i]] != testarr[i]:
                flag = 0
                break
            else:
                continue
            
        hashMapB = {}
        if flag == 1:
            for j in range(len(testarr)):
                if testarr[j] not in hashMapB:
                    hashMapB[testarr[j]] = pattern[j]
                elif hashMapB[testarr[j]] != pattern[j]:
                    flag = 0
                    break
                else:
                    continue
        
        return flag == 1
        