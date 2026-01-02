class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersections = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2 and not num1 in intersections:
                    intersections.append(num1)
        return intersections

class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_bool = defaultdict(bool)
        for num1 in nums1:
            if not num1 in num_to_bool:
                num_to_bool[num1] = False
        for num2 in nums2:
            if num2 in num_to_bool:
                num_to_bool[num2] = True
        return [k for k, v in num_to_bool.items() if v == True]
