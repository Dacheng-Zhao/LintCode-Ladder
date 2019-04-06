class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        # excceed time limit, need dict
        # if not words1 and not words2:
        #     return True
        # if not words1:
        #     return False
        # if not words2:
        #     return False
        
        # if len(words1) != len(words2):
        #     return False
        
        # for i in range(len(words1)):
        #     if words1[i] == words2[i]:
        #         continue
        #     notInDict = True
        #     for j in range(len(pairs)):
        #         if words1[i] in pairs[j]:
        #             if words2[i] in pairs[j]:
        #                 notInDict = False
        #     if notInDict:
        #         return False
    
        # return True
        
        if len(words1) != len(words2):
            return False
        
        dictMap = {}
        
        for i in range(len(pairs)):
            if pairs[i][0] not in dictMap:
                dictMap[pairs[i][0]] = [pairs[i][1]]
            else:
                dictMap[pairs[i][0]].append(pairs[i][1])
            if pairs[i][1] not in dictMap:
                dictMap[pairs[i][1]] = [pairs[i][0]]
            else:
                dictMap[pairs[i][1]].append(pairs[i][0])
        
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            elif words2[i] in dictMap[words1[i]]:
                continue
            else:
                return False
        
        return True
