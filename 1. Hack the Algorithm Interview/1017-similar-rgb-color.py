class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def similarRGB(self, color):
        # Write your code here
        selectable = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
        res = '#'
        for i in range(1, len(color), 2):
            minval = sys.maxsize
            temp = ''
            for j in range(len(selectable)):
                if abs(int(color[i : i + 2], 16) - int(selectable[j], 16)) < minval:
                    temp = selectable[j]
                    minval = abs(int(color[i : i + 2], 16) - int(selectable[j], 16))
            res += temp
        return res
        