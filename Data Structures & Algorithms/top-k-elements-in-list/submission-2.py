class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        arr = []
        for key, v in d.items():
            arr.append([v, key])
        arr.sort(reverse=True)
        sol = []
        for i in range(k):
            sol.append(arr[i][1])
        return sol