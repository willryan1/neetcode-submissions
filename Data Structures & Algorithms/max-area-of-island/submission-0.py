class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def calc(r, c, asf):
            if r < 0 or c < 0: return
            if r >= len(grid) or c >= len(grid[0]): return
            if grid[r][c] == 0: return
            grid[r][c] = 0
            asf[0] += 1

            calc(r + 1, c, asf)
            calc(r, c + 1, asf)
            calc(r - 1, c, asf)
            calc(r, c - 1, asf)

        solution = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = [0]
                    calc(i, j, area)
                    solution = max(solution, area[0])

        return solution