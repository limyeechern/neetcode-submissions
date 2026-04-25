class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1, 2, 2, 3, 3]
        # [1, 2, 4, 5]
        people.sort()
        count = 0
        l = 0

        for p in range(len(people) -1, -1, -1):
            if l > p:
                break
            if people[p] + people[l] <= limit:
                count += 1
                l += 1
            else:
                count += 1
        return count




            
