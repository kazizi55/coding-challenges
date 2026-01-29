# 動かず
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence_to_frequency_at_index = [0] * len(nums)
        subsequence_to_frequency_at_index[0] = defaultdict
        subsequence_to_frequency_at_index[0].current = 1
        subsequence_to_frequency_at_index[0].longest = 1

        for i in range(1, len(nums)):
            subsequence_to_frequency_at_index[i] = defaultdict
            subsequence_to_frequency_at_index[i].current = 0
            subsequence_to_frequency_at_index[i].longest = 0

            if nums[i] > num[i - 1]:
                subsequence_to_frequency_at_index[i].current += subsequence_to_frequency_at_index[i - 1].current
            if subsequence_to_frequency_at_index[i].current > subsequence_to_frequency_at_index[i - 1].longest:
                subsequence_to_frequency_at_index[i].longest = subsequence_to_frequency_at_index[i].current
        return subsequence_to_frequency_at_index[len(nums) - 1]
