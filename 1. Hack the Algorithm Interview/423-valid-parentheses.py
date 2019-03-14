class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        parenthesesDict = {')': '(', ']':'[', '}':'{'}
        stack = []
        
        for ele in s:
            if ele == '(' or ele == '[' or ele == '{':
                stack.append(ele)
            else:
                if len(stack) == 0:
                    return False
                else:
                    compare = stack.pop()
                    if compare != parenthesesDict[ele]:
                        return False
        return len(stack) == 0
        
        
        