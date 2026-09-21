class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        solution = 0
        
        def clear(c_i, c_j):
            if c_i < 0 or c_j < 0: return
            if c_i >= len(grid) or c_j >= len(grid[0]): return
            if grid[c_i][c_j] == '0': return
            
            grid[c_i][c_j] = '0'

            clear(c_i + 1, c_j)
            clear(c_i, c_j + 1)
            clear(c_i - 1, c_j)
            clear(c_i, c_j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    clear(i, j)
                    solution += 1
        
        return solution