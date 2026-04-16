# Wrong Answer　28 / 75 testcases passed
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums)):
            if index == len(nums) - 1:
                return
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)

class RevisedSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        checked_count = 0
        while checked_count < len(nums):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1
            checked_count += 1        
