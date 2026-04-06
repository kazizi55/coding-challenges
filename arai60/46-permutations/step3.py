class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []
        permutation = []
        def generate_permutation(rest_nums):
            if len(permutation) == len(nums):
                all_permutations.append(permutation.copy())
                return
            for index, rest_num in enumerate(rest_nums):
                permutation.append(rest_num)
                next_rest_nums = rest_nums[:index] + rest_nums[index + 1:]
                generate_permutation(next_rest_nums)
                permutation.pop()
        generate_permutation(nums)
        return all_permutations

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []
        stack = [([], nums)]
        while len(stack) > 0:
            permutation, rest_nums = stack.pop()
            if len(permutation) == len(nums):
                all_permutations.append(permutation)
                continue
            for index, rest_num in enumerate(rest_nums):
                next_permutation = permutation + [rest_num]
                next_rest_nums = rest_nums[:index] + rest_nums[index + 1:]
                stack.append((next_permutation, next_rest_nums))
        return all_permutations
