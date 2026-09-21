class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = ((r - l) // 2) + l
            print(mid)
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]