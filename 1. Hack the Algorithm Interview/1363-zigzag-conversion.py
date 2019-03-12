class Solution:
    """
    @param s: the given string
    @param numRows: the number of rows
    @return: the string read line by line
    """
    def convert(self, s, numRows):
        # Write your code here
        if numRows == 1 or numRows >= len(s):
            return s 
        
        holder = [''] * numRows
        
        dirction = 1 
        index = 0
        
        for ele in s:
            if index == 0:
                dirction = 1 
            if index == numRows - 1:
                dirction = -1 
            if dirction == 1:
                holder[index] += ele 
                index += 1 
            if dirction == -1:
                holder[index] += ele 
                index -= 1 
        return ''.join(holder)
            
