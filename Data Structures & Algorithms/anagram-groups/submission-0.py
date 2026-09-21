class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solutions = []
        exists = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s in exists:
                solutions[exists[s]].append(strs[i])
            else:
                solutions.append([strs[i]])
                exists[s] = len(solutions)-1
        return solutions