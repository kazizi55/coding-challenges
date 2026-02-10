class Solution1:
    OBSTACLE = 1

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        nums_paths = [[0] * num_cols for _ in range(num_rows)]
        for r in range(num_rows):
            if obstacleGrid[r][0] == self.OBSTACLE:
                break
            nums_paths[r][0] = 1
        for c in range(num_cols):
            if obstacleGrid[0][c] == self.OBSTACLE:
                break
            nums_paths[0][c] = 1
        for r in range(1, num_rows):
            for c in range(1, num_cols):
                if obstacleGrid[r][c] == self.OBSTACLE:
                    nums_paths[r][c] = 0
                    continue
                nums_paths[r][c] = nums_paths[r - 1][c] + nums_paths[r][c - 1]
        return nums_paths[-1][-1]

class Solution2:
    OBSTACLE = 1
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        nums_paths = [[0] * num_cols for _ in range(num_rows)]
        for r in range(num_rows):
            for c in range(num_cols):
                if obstacleGrid[r][c] == self.OBSTACLE:
                    nums_paths[r][c] = 0
                    continue
                if r == 0 and c == 0:
                    nums_paths[r][c] = 1
                    continue
                if r == 0:
                    nums_paths[r][c] = nums_paths[r][c - 1]
                    continue
                if c == 0:
                    nums_paths[r][c] = nums_paths[r - 1][c]
                    continue
                nums_paths[r][c] = nums_paths[r - 1][c] + nums_paths[r][c - 1]
        return nums_paths[-1][-1]
