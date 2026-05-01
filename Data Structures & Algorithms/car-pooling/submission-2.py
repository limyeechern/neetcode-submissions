class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        L, R = float("inf"), float("-inf")

        for _, start, end in trips:
            L = min(start, L)
            R = max(end, R)

        N = R - L + 1
        passengerChanged = [0] * (N + 1)

        for passenger, start, end in trips:
            passengerChanged[start - L] += passenger
            passengerChanged[end - L] -= passenger

        passengerState = 0
        for i in passengerChanged:
            passengerState += i
            if passengerState > capacity:
                return False

        return True