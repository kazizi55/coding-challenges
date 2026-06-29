# 自前の heap class を使う version
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_nums = MyHeap()
        for num in nums:
            self.top_k_nums.push(num)
            if len(self.top_k_nums) > self.k:
                self.top_k_nums.pop()

    def add(self, val: int) -> int:
        self.top_k_nums.push(val)
        if len(self.top_k_nums) > self.k:
            self.top_k_nums.pop()
        return self.top_k_nums.top()


# heapq を使う version (init で add する)
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


# heapq を使う version (init で heapify する)
from heapq import heapify, heappush


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_nums = nums
        heapify(self.top_k_nums)

    def add(self, val: int) -> int:
        heappush(self.top_k_nums, val)
        while len(self.top_k_nums) > self.k:
            heappop(self.top_k_nums)
        return self.top_k_nums[0]


# insortを使う version
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        insort(self.sorted_nums, val)
        return self.sorted_nums[-self.k]
