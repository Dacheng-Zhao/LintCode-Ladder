
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
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0
        
        start_meeting = []
        end_meeting = []
        
        for i in range(len(intervals)):
            start_meeting.append(intervals[i].start)
            end_meeting.append(intervals[i].end)
        
        start_meeting.sort()
        end_meeting.sort()
        count = 0
        startPointer = 0
        endPointer = 0
        res = 0
        
        while startPointer < len(start_meeting) and endPointer < len(end_meeting):
            if start_meeting[startPointer] <= end_meeting[endPointer]:
                count += 1 
                startPointer += 1 
            else:
                count -= 1 
                endPointer += 1 
            res = max(res, count)
        return res
