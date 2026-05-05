class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        stack = []
        for start, end in intervals:
            if not stack:
                stack.append([start, end])
                continue
            peek = stack[-1]
            if peek[1] >= start:
                peek = stack.pop()
                stack.append([min(peek[0], start), max(peek[1], end)])
            else:
                stack.append([start, end])

        return stack