class Solution1:
    def findMin(self, nums: List[int]) -> int:
        def find_min(left, right) -> int:
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                return find_min(left, mid)
            return find_min(mid + 1, right)
        return find_min(0, len(nums) - 1)

class Solution2:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
                continue
            left = mid + 1
        return nums[left]
