class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_amounts = [0] * len(nums)
        max_amounts[0] = nums[0]
        max_amounts[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            max_amounts[i] = max(max_amounts[i-2] + nums[i], max_amounts[i-1])
        return max_amounts[-1]

class Solution2:
    def rob(self, nums: List[int]) -> int:
        @cache
        def get_max_amount(i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[1], nums[0])
            return max(get_max_amount(i-2) + nums[i], get_max_amount(i-1))
        return get_max_amount(len(nums)-1)
