class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        WATER = 0
        LAND = 1
        VISITED = 2
        def get_island_area(r, c):
            if not(0 <= r < height and 0 <= c < width):
                return 0
            if grid[r][c] != LAND:
                return 0
            grid[r][c] = VISITED
            return (
                1 + get_island_area(r+1, c)
                + get_island_area(r, c+1)
                + get_island_area(r-1, c)
                + get_island_area(r, c-1)
            )
        
        max_area = 0
        for r in range(height):
            for c in range(width):
                if grid[r][c] != LAND:
                    continue
                area = get_island_area(r,c)
                max_area = max(max_area, area)
        return max_area

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        WATER = 0
        LAND = 1
        VISITED = 2
        def get_island_area(arg_r,arg_c) -> int:
            area = 0
            next_rc = deque([(arg_r, arg_c)])
            while next_rc:
                r, c = next_rc.popleft()
                if not(0 <= r < height and 0 <= c < width and grid[r][c] == LAND):
                    continue
                area += 1
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    new_r = r + dr
                    new_c = c + dc
                    next_rc.append((new_r, new_c))
                    grid[r][c] = VISITED
            return area
        
        max_area = 0
        for r in range(height):
            for c in range(width):
                if grid[r][c] != LAND:
                    continue
                max_area = max(max_area, get_island_area(r, c))
        return max_area

class Solution3:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        WATER = 0
        LAND = 1
        visited_grid = [[False] * width for _ in range(height)]
        def get_island_area(r, c) -> int:
            if not(0 <= r < height and 0 <= c < width):
                return 0
            if grid[r][c] != LAND or visited_grid[r][c] == True:
                return 0
            visited_grid[r][c] = True
            return (
                1 + get_island_area(r+1, c)
                + get_island_area(r, c+1)
                + get_island_area(r-1, c)
                + get_island_area(r, c-1)
            )

        max_area = 0
        for r in range(height):
            for c in range(width):
                if grid[r][c] != LAND or visited_grid[r][c] == True:
                    continue
                max_area = max(max_area, get_island_area(r,c))
        return max_area

class Solution4:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        WATER = 0
        LAND = 1
        visited_grid = [[False] * width for _ in range(height)]
        def get_island_area(arg_r, arg_c) -> int:
            area = 0
            next_rc = deque([(arg_r, arg_c)])
            while next_rc:
                r, c = next_rc.popleft()
                if not(0 <= r < height and 0 <= c < width):
                    continue
                if grid[r][c] != LAND or visited_grid[r][c] == True:
                    continue
                area += 1
                for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                    new_r = r + dr
                    new_c = c + dc
                    next_rc.append((new_r, new_c))
                    visited_grid[r][c] = True
            return area
        
        max_area = 0
        for r in range(height):
            for c in range(width):
                if grid[r][c] != LAND or visited_grid[r][c] == True:
                    continue
                max_area = max(max_area, get_island_area(r, c))
        return max_area
