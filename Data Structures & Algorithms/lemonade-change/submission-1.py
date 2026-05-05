class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        wallet = {5: 0, 10: 0}

        for b in bills:
            if b == 5:
                wallet[5] += 1
            elif b == 10:
                if not wallet[5]:
                    return False
                wallet[5] -= 1
                wallet[10] += 1
            else:
                if wallet[10] and wallet[5]:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                else:
                    return False
            
        return True