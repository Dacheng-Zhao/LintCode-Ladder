"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        if not intervals or not intervals[0]:
            return []
            
        res = []
        oneDarray = []
        
        for i in range(len(intervals)):
            for j in range(len(intervals[i])):
                oneDarray.append(intervals[i][j])
        
        oneDarray.sort(key=lambda x : x.start)
        
        res.append(oneDarray[0])
        for k in range(1, len(oneDarray)):
            if res[-1].end >= oneDarray[k].start:
                res[-1].end = max(res[-1].end, oneDarray[k].end)
            else:
                res.append(oneDarray[k])
        
        return res
        