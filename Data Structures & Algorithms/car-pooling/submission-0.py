class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        L, R = float('inf'), float("-inf")

        for _, left, right in trips:
            L = min(L, left)
            R = max(R, right)

        N = R - L + 1
        passengerChange = [0] * (N + 1)

        for passenger, left, right in trips:
            passengerChange[left - L] += passenger
            passengerChange[right - L] -= passenger

        currPassenger = 0
        for i in passengerChange:
            currPassenger += i
            if currPassenger > capacity:
                return False
        return True