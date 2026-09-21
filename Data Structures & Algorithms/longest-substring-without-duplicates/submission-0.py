class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        rep = set()
        sol = 0
        for i in range(len(s)):
            if s[i] in rep:
                while j < i and s[j] != s[i]:
                    rep.remove(s[j])
                    j += 1
                j += 1
            rep.add(s[i])
            sol = max(sol, i - j + 1)
        return sol