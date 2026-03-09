# 4 / 196 testcases passed
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[target] == nums[right]:
                return nums[right]
            if nums[target] < nums[mid]:    
                right = mid
                continue
            left = mid + 1
        return -1

