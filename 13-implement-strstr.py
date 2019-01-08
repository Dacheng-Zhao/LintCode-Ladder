class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        
        for i in range(len(source) - len(target) + 1):
            if source[i : i + len(target)] == target: return i
        return -1

test = Solution()
print(test.strStr('source', 'sou'))
print(test.strStr('source', 'tar'))