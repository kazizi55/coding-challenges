class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_total = 0
        cumulative_total_to_frequency = defaultdict(int)
        cumulative_total_to_frequency[0] = 1
        subarray_total = 0
        for num in nums:
            cumulative_total += num
            subarray_total += cumulative_total_to_frequency[cumulative_total - k]
            cumulative_total_to_frequency[cumulative_total] += 1
        return subarray_total
