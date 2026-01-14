class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER = "0"
        LAND = "1"
        VISITED = "2"
        height = len(grid)
        width = len(grid[0])
        def mark_islands_visited(i, j):
            if not(0 <= i < height and 0 <= j < width):
                return
            if grid[i][j] != LAND:
                return
            grid[i][j] = VISITED
            mark_islands_visited(i-1, j)
            mark_islands_visited(i, j-1)
            mark_islands_visited(i+1, j)
            mark_islands_visited(i, j+1)
        
        num_of_islands = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] != LAND:
                    continue
                mark_islands_visited(i,j)
                num_of_islands += 1
        return num_of_islands
