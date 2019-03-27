class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        if not words:
            return True
        
        n = len(words)
        row = 0
        
        while row < n:
            l = len(words[row])
            col = 0
            while col < l:
                if words[row][col] != words[col][row]:
                    return False
                col += 1 
            row += 1
        return True
        
        
