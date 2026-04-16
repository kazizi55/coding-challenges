class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_putting_index = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                continue
            nums[non_zero_putting_index] = nums[index]
            non_zero_putting_index += 1
        for index in range(non_zero_putting_index, len(nums)):
            nums[index] = 0

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_putting_index = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                continue
            nums[index], nums[non_zero_putting_index] = nums[non_zero_putting_index], nums[index]
            non_zero_putting_index += 1
