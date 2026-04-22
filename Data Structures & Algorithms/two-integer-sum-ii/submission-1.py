class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            summation = numbers[l] + numbers[r]
            if summation > target:
                r -= 1
                continue
            elif summation < target:
                l += 1
                continue
            else:
                return [l + 1, r + 1]
            