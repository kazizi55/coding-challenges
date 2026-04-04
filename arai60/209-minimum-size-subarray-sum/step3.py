class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        prefixed_sum = 0
        min_length = sys.maxsize
        for right in range(len(nums)):
            prefixed_sum += nums[right]
            while prefixed_sum >= target:
                min_length = min(min_length, right - left + 1)
                prefixed_sum -= nums[left]
                left += 1
        if min_length == sys.maxsize:
            return 0
        return min_length
