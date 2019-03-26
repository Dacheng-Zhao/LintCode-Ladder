class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """
    def twitchWords(self, str):
        # Write your code here
        if not str:
            return []
        res = []
        count = 1 
        temp = []
        
        for i in range(len(str)):
            if i != 0  and str[i] == str[i - 1]:
                count += 1 
                if count == 3:
                    temp = [i - 2]
            else:
                if count >= 3:
                    temp.append(i - 1)
                    res.append(temp)
                    temp = []
                count = 1
        if count >= 3:
            res.append([len(str) - count, len(str) - 1])
        return res
        