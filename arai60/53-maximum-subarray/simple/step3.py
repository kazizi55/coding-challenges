class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix_sum = 0
        max_sum = nums[0]
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
        return max_sum

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        INITIAL_VAL = -math.inf
        max_sum_at_index = [INITIAL_VAL] * len(nums)
        max_sum_at_index[0] = nums[0]
        for i in range(1, len(nums)):
            max_sum_at_index[i] = max(
                max_sum_at_index[i - 1] + nums[i],
                nums[i]
            )
        return max(max_sum_at_index)

class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            current_max = max(current_max + nums[i], nums[i])
            global_max = max(global_max, current_max)
        return global_max
