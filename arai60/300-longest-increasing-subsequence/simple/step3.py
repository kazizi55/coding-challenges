class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_lengths = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_lengths[i] = max(max_lengths[i], max_lengths[j] + 1)
        return max(max_lengths)

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        min_ends = []
        for num in nums:
            insert_index = bisect_left(min_ends, num)
            if insert_index <= len(min_ends) - 1:
                min_ends[insert_index] = num
                continue
            min_ends.append(num)
        return len(min_ends)

class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bisect_left_func(list_, insert_val) -> int:
            left = 0
            right = len(list_)
            while left < right:
                middle = (left + right) // 2
                if insert_val <= list_[middle]:
                    right = middle
                    continue
                left = middle + 1
            return left
        
        min_ends = []
        for num in nums:
            insert_index = bisect_left_func(min_ends, num)
            if insert_index <= len(min_ends) - 1:
                min_ends[insert_index] = num
                continue
            min_ends.append(num)
        return len(min_ends)
