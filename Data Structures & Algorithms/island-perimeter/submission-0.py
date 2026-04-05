class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        borders = 0
        for i in range(rowLen):
            for j in range(colLen):
                print(rowLen, colLen)
                if grid[i][j] == 0:
                    continue
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    borders += 1
                if j + 1 >= colLen or grid[i][j + 1] == 0:
                    borders += 1
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    borders += 1
                if i + 1 >= rowLen or grid[i + 1][j] == 0:
                    borders += 1
        return borders