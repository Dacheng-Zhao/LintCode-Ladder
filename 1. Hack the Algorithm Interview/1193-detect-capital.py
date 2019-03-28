class Solution:
    """
    @param word: a string
    @return: return a boolean
    """
    def detectCapitalUse(self, word):
        # write your code here
        if not word:
            return True 
            
        for i in range(len(word)):
            if i != 0 and ord(word[i]) < 97 and ord(word[i - 1]) > 96:
                return False
            if i == len(word) - 1 and i - 1 >= 0:
                if ord(word[i]) > 96 and ord(word[i - 1]) <= 96:
                    return False
        return True
