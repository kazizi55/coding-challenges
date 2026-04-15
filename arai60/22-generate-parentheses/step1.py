class RevisedSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_combinations = []
        def traverse_combination(index, combination, open_count, close_count):
            if index == n * 2:
                if open_count == n and close_count == n:
                    all_combinations.append(''.join(combination))
                return
            if open_count < n:
                combination.append('(')
                traverse_combination(
                    index + 1,
                    combination,
                    open_count + 1,
                    close_count
                )
                combination.pop()
            if close_count < open_count:
                combination.append(')')
                traverse_combination(
                    index + 1,
                    combination,
                    open_count,
                    close_count + 1
                )
                combination.pop()
        traverse_combination(0, [], 0, 0)
        return all_combinations
