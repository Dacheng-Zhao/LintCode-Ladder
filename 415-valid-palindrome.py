import string
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        arrayHolder = []
        for c in s:
            if c.isalpha() or c.isdigit():
                arrayHolder += [c.lower()]
        return arrayHolder[::-1] == arrayHolder

    def isPalindrome2(self, s):
        allowed = set(string.ascii_lowercase + string.digits)
        s = [c for c in s.lower() if c in allowed]

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindrome3(self, s):
        # using reverse
        reversed_string = ''
        nospace_string = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                nospace_string += s[i].lower()
            if s[len(s) - i - 1].isalpha() or s[len(s) - i - 1].isdigit():
                reversed_string += s[len(s) - i - 1].lower()
        return nospace_string == reversed_string
        

test = Solution()
print(test.isPalindrome2('A man, a plan, a canal: Panama'))
print(test.isPalindrome2('race a car'))