# 通らない
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                right = mid
                continue
            left = mid + 1
        return nums[left]


class RevisedSolution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
                continue
            left = mid + 1
        return nums[left]
