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

    def strStr2(self, source, target):
        for i in range(len(source) - len(target) + 1):
            # for/else or while/else for python
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:
                return i
        return -1

test = Solution()
print(test.strStr2('source', 'sou'))
print(test.strStr2('source', 'tar'))
print(test.strStr2('source', 'rce'))
print(test.strStr2('source', 'rse'))