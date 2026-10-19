"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # print(intervals)
        intervals.sort(key = lambda i:i.start)
        # print(intervals)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].end:
                return False
        return True
