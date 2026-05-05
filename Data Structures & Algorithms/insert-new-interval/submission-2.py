class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # 3 cases
        # [0, 1], [2,5]
        # [2,5], [6,7]
        # [2,5], [3,4]

        for i, interval in enumerate(intervals):
            start, end = interval[0], interval[1]

            if newInterval[0] > end:
                res.append(interval)
            elif newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [
                    min(newInterval[0], start),
                    max(newInterval[1], end)
                ]
        res.append(newInterval)

        return res