# 辞書型を使う
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = defaultdict(int)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[nums[i]] = i
        return []

# 二重ループを使う
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
