class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            if r < 0 or c < 0: return 0 
            if r >= len(grid) or c >= len(grid[0]): return 0
            if grid[r][c] == 0: return 0
            grid[r][c] = 0

            return 1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)

        solution = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    solution = max(solution, dfs(i, j))

        return solution