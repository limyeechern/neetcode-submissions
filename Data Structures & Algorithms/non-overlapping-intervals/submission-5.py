class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        # intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: (x[1],x[0]))
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                count += 1
                continue
            prevEnd = end
        
        return count