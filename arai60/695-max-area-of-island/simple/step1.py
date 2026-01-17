class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        WATER = 0
        LAND = 1
        VISITED = 2
        height = len(grid)
        width = len(grid[0])
        def mark_islands_visited_calculate_total(i, j):
            if not(0 <= i < height and 0 <= j < width):
                return 0
            if grid[i][j] != LAND:
                return 0
            grid[i][j] = VISITED
            total = 1
            total += mark_islands_visited_calculate_total(i-1, j)
            total += mark_islands_visited_calculate_total(i, j-1)
            total += mark_islands_visited_calculate_total(i+1, j)
            total += mark_islands_visited_calculate_total(i, j+1)
            return total
        
        max_area_of_island = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] != LAND:
                    continue
                total = mark_islands_visited_calculate_total(i, j)
                if max_area_of_island < total:
                    max_area_of_island = total
        return max_area_of_island
