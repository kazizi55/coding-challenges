class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frequency = defaultdict(int)
        for num in nums:
            nums_frequency[num] += 1
        
        sorted_nums_frequency = sorted(nums_frequency, key=nums_frequency.get, reverse=True)
        top_k_nums = sorted_nums_frequency[:k]
        return top_k_nums
    
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency = defaultdict(int)
        for num in nums:
            num_frequency[num] += 1
        
        desc_sorted_num_frequency = []
        for num, fre in num_frequency.items():
            heapq.heappush(desc_sorted_num_frequency, (fre, num))
            if len(desc_sorted_num_frequency) > k:
                heapq.heappop(desc_sorted_num_frequency)
        
        top_k_nums = []
        while desc_sorted_num_frequency:
            _, num = heapq.heappop(desc_sorted_num_frequency)
            top_k_nums.append(num)
        return top_k_nums
