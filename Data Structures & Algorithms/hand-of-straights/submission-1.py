class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = {}
        for num in hand:
            d[num] = d.get(num, 0) + 1
        
        for card in sorted(hand):
            if d[card] == 0:
                continue
            
            for i in range(groupSize):
                target = card + i
                if d.get(target, 0) == 0:
                    return False
                d[target] -= 1
        return True
