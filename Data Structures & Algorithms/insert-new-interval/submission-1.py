class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        
        res = []
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue
            peek = res[-1]
            current = intervals[i]
            if peek[1] >= current[0]:
                peek = res.pop()
                res.append([peek[0], max(peek[1], current[1])])
                continue
            res.append(current)

        return res
