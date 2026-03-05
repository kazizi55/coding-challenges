# TLE
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(start, end):
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return binary_search(start, mid)
            if target > nums[mid]:
                return binary_search(mid, end)
        return binary_search(0, len(nums) - 1)

class RevisedSolution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(start, end):
            if start > end:
                return start
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return binary_search(start, mid - 1)
            if target > nums[mid]:
                return binary_search(mid + 1, end)
        return binary_search(0, len(nums) - 1)
