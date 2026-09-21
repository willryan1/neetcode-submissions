class Solution:
    def trap(self, height: List[int]) -> int:
        solution = 0
        left = [0] * len(height)
        right = [0] * len(height)
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        for i in range(1, len(height)-1):
            if height[i] < min(left[i], right[i]):
                solution += min(left[i], right[i]) - height[i]
        return solution