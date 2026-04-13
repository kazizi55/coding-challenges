# Time Limit Exceeded 9 / 10 testcases passed
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        stack = [([], nums)]
        while len(stack) > 0:
            subset, rest_nums = stack.pop()
            sorted_subset = sorted(subset)
            if not(sorted_subset in all_subsets):
                all_subsets.append(sorted_subset)
            for index, rest_num in enumerate(rest_nums):
                next_rest_nums = rest_nums[:index] + rest_nums[index + 1:]
                next_subset = subset + [rest_num]
                stack.append((next_subset, next_rest_nums))
        return all_subsets
