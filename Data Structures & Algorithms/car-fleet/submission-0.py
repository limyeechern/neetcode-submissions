class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()

        stack = []
        for i in range(len(pair) - 1, -1, -1):
            timeTaken = (target - pair[i][0]) / pair[i][1]
            if not stack:
                stack.append(timeTaken)
                continue 
            if stack[-1] >= timeTaken:
                continue
            else:
                stack.append(timeTaken)

        return len(stack)