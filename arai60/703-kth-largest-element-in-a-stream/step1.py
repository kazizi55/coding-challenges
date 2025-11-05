# Initial Solution
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.list = sorted(nums, reverse=True)
        self.k = k
        

    def add(self, val: int) -> int:
        self.list.append(val)
        self.list = sorted(self.list, reverse=True)
        return self.list[self.k - 1]
