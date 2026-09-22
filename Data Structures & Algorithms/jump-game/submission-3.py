class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = [False] * len(nums)
        reach[0] = True
        for i in range(len(nums)):
            if reach[i]:
                c = i + 1
                while c < len(reach) and c <= i + nums[i]:
                    reach[c] = True
                    c += 1
        return reach[len(reach)-1]