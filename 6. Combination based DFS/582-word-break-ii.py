class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    # def wordBreak(self, s, wordDict):
    #     # write your code here
    #     if not self.canBreak(s, wordDict):
    #         return []
    #     result_lists = self.breakWord(s, 0, wordDict, {})
    #     return [" ".join(result) for result in result_lists]
        
    # def canBreak(self, s, wordDict):
    #     # write your code here
    #     if len(wordDict) == 0:
    #         return len(s) == 0
            
    #     can_make = [False] * (len(s) + 1)
    #     can_make[0] = True
    #     maxLength = max([len(w) for w in wordDict])
        
    #     for i in range(1, len(s) + 1):
    #         for j in range(i - 1, -1, -1):
    #             if i - j > maxLength:
    #                 break
    #             if can_make[j] and s[j:i] in wordDict:
    #                 can_make[i] = True
    #                 break
    #     return can_make[-1]
        
    # def breakWord(self, s, left, wordDict, memo):
    #     if left >= len(s):
    #         return [[]]
    #     if left in memo:
    #         return memo[left]
                
    #     results = []
    #     for i in range(left + 1, len(s) + 1):
    #         prefix = s[left : i]
    #         suffix_breaks = self.breakWord(s, i, wordDict, memo)
    #         if suffix_breaks and prefix in wordDict:
    #             for suffix_break in suffix_breaks:
    #                 results.append([prefix] + suffix_break)
                        
    #     memo[left] = results[:]
    #     return results
    
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
    
    # 找到 s 的所有切割方案并 return
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
            
        if len(s) == 0:
            return []
            
        partitions = []
        
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)
                
        if s in wordDict:
            partitions.append(s)
            
        memo[s] = partitions
        return partitions
                