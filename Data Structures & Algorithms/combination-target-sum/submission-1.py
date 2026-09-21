class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions = []

        def generate(c_arr, c_sum, start):
            if c_sum == target:
                solutions.append(c_arr[:])
                return
            elif c_sum > target:
                return
            elif start >= len(nums):
                return
            
            for i in range(start, len(nums)):
                c_arr.append(nums[i])
                generate(c_arr, c_sum + nums[i], i)
                c_arr.pop()
        
        generate([], 0, 0)
        return solutions