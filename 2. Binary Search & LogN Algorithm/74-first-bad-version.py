#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here

        start = 0
        end = n

        while start + 1 < end:
            mid = start + (end - start) // 2
            if SVNRepo.isBadVersion(mid) == True:
                end = mid
            else:
                start = mid
        
        if SVNRepo.isBadVersion(start) == True:
            return start
        else:
            return end