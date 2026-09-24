class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        result = []

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        n_l = float('inf')
        n_r = float('-inf')
        while i < n and intervals[i][0] <= newInterval[1]:
            n_l = min(n_l, intervals[i][0], newInterval[0])
            n_r = max(n_r, intervals[i][1], newInterval[1])
            i += 1
        if n_l == float('inf'):
            result.append(newInterval)
        else:
            result.append([n_l, n_r])
        
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result