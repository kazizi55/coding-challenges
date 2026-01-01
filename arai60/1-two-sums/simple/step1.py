# 通らない
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)
        for i in range(len(nums)):
            if num_dict[nums[i]]:
                return [num_dict[nums[i]], i]
            num_dict[target - nums[i]] = i
