"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        for i in range(n):
            for j in range(i):
                interval1 = intervals[i]
                interval2 = intervals[j]

                if not (interval1.start >= interval2.end or interval1.end <= interval2.start):
                    return False

        return True