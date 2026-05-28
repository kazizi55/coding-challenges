class Solution1:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rfind_first_decreasing():
            for i in range(len(nums) -2, -1, -1):
                if nums[i] < nums[i+1]:
                    return i
            return -1
        def rfind_greater_than(target):
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > target:
                    return i
        def reverse_in_range(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        pivot_index = rfind_first_decreasing()
        if pivot_index == -1:
            nums.reverse()
            return
        swap_index = rfind_greater_than(nums[pivot_index])
        nums[pivot_index], nums[swap_index] = nums[swap_index], nums[pivot_index]
        reverse_in_range(pivot_index + 1, len(nums) - 1)