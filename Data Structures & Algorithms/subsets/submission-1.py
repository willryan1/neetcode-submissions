class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        
        def generate(current, start):
            solution.append(current[:])
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                generate(current, i+1)
                current.pop()
            
        generate([], 0)
        return solution