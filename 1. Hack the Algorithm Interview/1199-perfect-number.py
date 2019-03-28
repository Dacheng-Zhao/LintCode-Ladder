class Solution:
    """
    @param num: an integer
    @return: returns true when it is a perfect number and false when it is not
    """
    def checkPerfectNumber(self, num):
        # write your code here
        if not num:
            return False 
        
        numSum = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                numSum += i 
                numSum += num // i
            if numSum == num:
                return True
            elif numSum > num:
                return False 
            i += 1
        return False
