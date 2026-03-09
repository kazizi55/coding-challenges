class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                    continue
                right = mid - 1
                continue
            if nums[left] <= target < nums[mid]:
                right = mid - 1
                continue
            left = mid + 1
        return -1

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        def generate_priority_value(num):
            return (num <= nums[-1], target <= num)
        index = bisect_left(nums, generate_priority_value(target), key=generate_priority_value)
        if nums[index] == target:
            return index
        return -1
