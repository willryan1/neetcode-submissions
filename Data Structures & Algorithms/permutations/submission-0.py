class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []
        self.gen(nums, [], solution, set())
        return solution
        
    def gen(self, nums, current, solution, used):
        if len(current) == len(nums):
            solution.append(current[:])
            return
        for i in range(len(nums)):
            if i not in used:
                current.append(nums[i])
                used.add(i)
                self.gen(nums, current, solution, used)
                current.pop()
                used.remove(i)
        