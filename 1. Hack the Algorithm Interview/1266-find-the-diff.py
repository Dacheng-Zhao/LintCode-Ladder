class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """
    def findTheDifference(self, s, t):
        # Write your code here
        ls = len(s)
        scode = 0
        tcode = 0
        
        for i in range(ls):
            scode += ord(s[i])
            tcode += ord(t[i])
        
        tcode += ord(t[-1])
        
        return chr(tcode - scode)
        