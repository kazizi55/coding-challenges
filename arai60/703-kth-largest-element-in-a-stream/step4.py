# 自前の heap class を使う version (init の for ループで早期 continue)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_nums = MyHeap()
        for num in nums:
            self.top_k_nums.push(num)
            if len(self.top_k_nums) <= self.k:
                continue
            self.top_k_nums.pop()

    def add(self, val: int) -> int:
        self.top_k_nums.push(val)
        if len(self.top_k_nums) > self.k:
            self.top_k_nums.pop()
        return self.top_k_nums.top()

# heapq を使う version (heapq を package のみ import した & インスタンス変数の命名を変えた)
import heapq

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
