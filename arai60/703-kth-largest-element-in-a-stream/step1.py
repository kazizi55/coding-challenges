class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)
        return self.nums[self.k - 1]

# min-listを内部的に保持する
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.sorted_nums = sorted(nums)

    def add(self, val: int) -> int:
        self.sorted_nums.append(val)
        self.sorted_nums.sort()
        return self.sorted_nums[-self.k]

# heapqを使ってinitでaddする
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

# heapqを使ってheapifyでinitしてadd内で要素数の調整をする
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.largest_nums = nums
        heapq.heapify(self.largest_nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.largest_nums, val)
        while len(self.largest_nums) > self.capacity:
            heapq.heappop(self.largest_nums)
        return self.largest_nums[0]

# bisect.insortを使って要素挿入 & sortを高速に行う
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.sorted_nums = sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.sorted_nums, val)
        return self.sorted_nums[-self.k]