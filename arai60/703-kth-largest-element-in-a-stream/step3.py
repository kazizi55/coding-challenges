from heapq import heappush, heappop


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_nums = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.top_k_nums, val)
        if len(self.top_k_nums) > self.k:
            heappop(self.top_k_nums)
        return self.top_k_nums[0]
