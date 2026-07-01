class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.largest_nums = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.largest_nums, val)
        if len(self.largest_nums) > self.capacity:
            heapq.heappop(self.largest_nums)
        return self.largest_nums[0]