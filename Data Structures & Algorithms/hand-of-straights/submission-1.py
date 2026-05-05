class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        expectedHands = len(hand) // groupSize

        hashmap = {}

        for h in hand:
            hashmap[h] = hashmap.get(h,0) + 1
        
        currentMin = min(hand)
        while expectedHands > 0:
            for i in range(currentMin, currentMin + groupSize):
                if i not in hashmap or hashmap[i] == 0:
                    return False
                hashmap[i] -= 1
                if hashmap[currentMin] == 0:
                    del hashmap[currentMin]
                    if hashmap:
                        currentMin = min(hashmap.keys())
            expectedHands -= 1
        return True




        