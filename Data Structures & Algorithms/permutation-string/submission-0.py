class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2: return False
        
        set1 = [0] * 26
        set2 = [0] * 26

        for i in range(l1):
            set1[ord(s1[i]) - ord('a')] += 1
            set2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(l1, l2):
            if set1 == set2:
                return True
            
            set2[ord(s2[i-l1]) - ord('a')] -= 1
            set2[ord(s2[i]) - ord('a')] += 1
        if set1 == set2:
            return True
        return False