class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        combination = []
        def traverse_combination(open_num, close_num):
            if open_num == n and close_num == n:
                result.append(''.join(combination))
                return
            if open_num < n:
                combination.append('(')
                traverse_combination(open_num + 1, close_num)
                combination.pop()
            if close_num < open_num:
                combination.append(')') 
                traverse_combination(open_num, close_num + 1)
                combination.pop()
        traverse_combination(0, 0)
        return result

class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        result = []
        for num_pairs_A in range(n):
            for A in self.generateParenthesis(num_pairs_A):
                for B in self.generateParenthesis(n - 1 - num_pairs_A):
                    result.append(f'({A}){B}')
        return result
