"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        startTime = float("inf")
        endTime  = float("-inf")
        
        for interval in intervals:
            start = interval.start
            end = interval.end
            startTime = min(start, startTime)
            endTime = max(end, endTime)

        print(startTime, endTime)
        ans = [0] * (endTime - startTime + 1)

        for interval in intervals:
            start = interval.start - startTime
            end = interval.end - startTime
            ans[start] += 1 
            ans[end] -= 1
        
        meetingState = 0
        meetingRooms = 0
        for time in ans:
            meetingState += time
            meetingRooms = max(meetingState, meetingRooms)

        return meetingRooms