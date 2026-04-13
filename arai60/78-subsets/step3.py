class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        for bit_mask in range(1 << len(nums)):
            subset = []
            for i in range(len(nums)):
                if bit_mask & (1 << i):
                    subset.append(nums[i])
            all_subsets.append(subset)
        return all_subsets

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        def traverse_nums(index, subset):
            if index == len(nums):
                all_subsets.append(subset.copy())
                return
            traverse_nums(index + 1, subset)
            subset.append(nums[index])
            traverse_nums(index + 1, subset)
            subset.pop()
        traverse_nums(0, [])
        return all_subsets

class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        stack = [(0, [])]
        while len(stack) > 0:
            index, subset = stack.pop()
            if index == len(nums):
                all_subsets.append(subset.copy())
                continue
            stack.append((index + 1, subset))
            added_subset = subset + [nums[index]]
            stack.append((index + 1, added_subset))
        return all_subsets
