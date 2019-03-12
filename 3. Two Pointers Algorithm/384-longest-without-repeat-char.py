class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        seen = {}
        maxlen = 0
        
        while right < len(s):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1 
            else:
                maxlen = max(maxlen, right - left + 1)
            seen[s[right]] = right
            right += 1
        return maxlen
                
        