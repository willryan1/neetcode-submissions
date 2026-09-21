class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = []
        stack = deque()
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if not stack:
                solution.append(0)
            else:
                solution.append(stack[-1][1] - i)
            stack.append([temperatures[i], i])
        return solution[::-1]