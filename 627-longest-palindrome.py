import collections

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        max_length = 0
        letters = list()

        for c in s:
            if c in letters:
                max_length += 2
                letters.remove(c)
            else:
                letters.append(c)
        return max_length + int(len(letters) > 0)

    def longestPalindrome2(self, s):
        max_length = 0
        for n in collections.Counter(s).values():
            max_length += n - n % 2
        return max_length + int(max_length < len(s))

test = Solution()
print(test.longestPalindrome2('aabbcc'))
print(test.longestPalindrome2('abc'))