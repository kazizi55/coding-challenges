class Solution1:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2 or k == 0:
            return res
        
        sum_and_index_queue = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(sum_and_index_queue, (nums1[i] + nums2[0], i, 0))
        
        while sum_and_index_queue and len(res) < k:
            _, i, j = heapq.heappop(sum_and_index_queue)
            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(sum_and_index_queue, (nums1[i] + nums2[j+1], i, j+1))
        return res

class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        candidates = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()

        def is_necessary_to_add(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return False
            if i == 0 or j == 0:
                return True
            return (i-1, j) in visited and (i, j-1) in visited
        
        def add_to_candidates_if_necessary(i, j):
            if is_necessary_to_add(i, j):
                heapq.heappush(candidates, (nums1[i] + nums2[j], i, j))
        
        pairs = []
        while candidates and len(pairs) < k:
            _, i, j = heapq.heappop(candidates)
            pairs.append([nums1[i], nums2[j]])
            visited.add((i, j))
            add_to_candidates_if_necessary(i+1, j)
            add_to_candidates_if_necessary(i, j+1)
        return pairs
