"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals:
            return True
        
        intervals = sorted(intervals, key=lambda k : k.start)
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if res[-1].end > intervals[i].start:
                return False
            else:
                res.append(intervals[i])
        return True
            
        
