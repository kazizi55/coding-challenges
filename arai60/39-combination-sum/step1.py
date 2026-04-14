# TLE
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_combinations = []
        def traverse_combination(index, combination):
            if sum(combination) > target:
                return
            if sum(combination) == target:
                all_combinations.append(combination.copy())
                return
            traverse_combination(index + 1, combination)
            combination.append(candidates[index])
            traverse_combination(index + 1, combination)
            combination.pop()
        traverse_combination(0, [])
        return all_combinations

class RevisedSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_combinations = []
        def traverse_combination(index, combination, current_sum):
            if current_sum == target:
                all_combinations.append(combination.copy())
                return
            if current_sum > target or index == len(candidates):
                return
            combination.append(candidates[index])
            traverse_combination(index, combination, current_sum + candidates[index])
            combination.pop()
            traverse_combination(index + 1, combination, current_sum)
        traverse_combination(0, [], 0)
        return all_combinations
