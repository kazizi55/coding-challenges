# 25 / 42 testcases passed
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row_length = len(obstacleGrid)
        column_length = len(obstacleGrid[0])
        nums_of_paths = [[0] * column_length for _ in range(row_length)]
        for r in range(row_length):
            for c in range(column_length):
                if obstacleGrid[r][c] == 1:
                    continue
                if r == 0 or c == 0:
                    nums_of_paths[r][c] = 1
                    continue
                nums_of_paths[r][c] = nums_of_paths[r - 1][c] + nums_of_paths[r][c - 1]
        return nums_of_paths[-1][-1]

class RevisedSolution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        row_length = len(obstacleGrid)
        column_length = len(obstacleGrid[0])
        nums_of_paths = [[0] * column_length for _ in range(row_length)]
        nums_of_paths[0][0] = 1
        for r in range(row_length):
            for c in range(column_length):
                if (r == 0 and c == 0) or obstacleGrid[r][c] == 1:
                    continue
                if r == 0 and c > 0:
                    nums_of_paths[r][c] = nums_of_paths[r][c - 1]
                    continue
                if c == 0 and r > 0:
                    nums_of_paths[r][c] = nums_of_paths[r - 1][c]
                    continue
                nums_of_paths[r][c] = nums_of_paths[r - 1][c] + nums_of_paths[r][c - 1]
        return nums_of_paths[-1][-1]
