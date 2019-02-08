"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        res = []
        if not list1:
            return list2
        if not list2:
            return list1
        
        i, j = 0, 0
        
        while i < len(list1) or j < len(list2):
            if i == len(list1):
                self.merge(res, list2[j])
                j += 1 
            elif j == len(list2):
                self.merge(res, list1[i])
                i += 1 
            elif list1[i].start < list2[j].start:
                self.merge(res, list1[i])
                i += 1 
            else:
                self.merge(res, list2[j])
                j += 1 
        return res
        
    def merge(self, res, interval):
        if not res:
            res.append(interval)
        if res[-1].end >= interval.start:
            res[-1].end = max(res[-1].end, interval.end)
        else:
            res.append(interval)
    
            
                
        