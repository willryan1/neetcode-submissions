class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = set()
        for i in range(len(nums)):
            if nums[i] in d:
                return nums[i]
            d.add(nums[i])
        return -1