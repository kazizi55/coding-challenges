class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_combinations = []
        def traverse_combination(index, total, combination):
            if index == len(candidates) or total > target:
                return
            if total == target:
                all_combinations.append(combination.copy())
                return
            combination.append(candidates[index])
            traverse_combination(index, total + candidates[index], combination)
            combination.pop()
            traverse_combination(index + 1, total, combination)
        traverse_combination(0, 0, [])
        return all_combinations

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_combinations = []
        stack = [(0, 0, [])]
        while len(stack) > 0:
            index, total, combination = stack.pop()
            if index == len(candidates) or total > target:
                continue
            if total == target:
                all_combinations.append(combination.copy())
                continue
            stack.append((index, total + candidates[index], combination + [candidates[index]]))
            stack.append((index + 1, total, combination))
        return all_combinations
