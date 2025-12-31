# 動かない
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        sum_pairs = defaultdict(list)
        for num1 in nums1:
            for num2 in nums2:
                pair_sum = num1 + num2
                if sum_pairs[pair_sum]:
                    sum_pairs[pair_sum].append([num1, num2])
                    continue
                sum_pairs[pair_sum] = list([num1, num2])
                
        
        sorted_sum_pairs = sorted(sum_pairs)
        top_k_smallest_sums = []
        for sum_pair in sorted_sum_pairs:
            heapq.heappush(top_k_smallest_sums, *sum_pair)
            while len(top_k_smallest_sums) > k:
                heapq.heappop(top_k_smallest_sums)
        return top_k_smallest_sums
