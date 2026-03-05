class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def my_bisect_left(left, right) -> int:
            if left == right:
                return left
            mid = (left + right) // 2
            if target <= nums[mid]:
                return my_bisect_left(left, mid)
            return my_bisect_left(mid + 1, right)
        return my_bisect_left(0, len(nums))

class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def my_bisect_left(left, right) -> int:
            if left > right:
                return left
            mid = (left + right) // 2
            if target <= nums[mid]:
                return my_bisect_left(left, mid - 1)
            return my_bisect_left(mid + 1, right)
        return my_bisect_left(0, len(nums) - 1) 

class Solution3:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
                continue
            left = mid + 1
        return left
