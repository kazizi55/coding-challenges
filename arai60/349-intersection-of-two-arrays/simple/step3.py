class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return list(nums1_set & nums2_set)

class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        intersections = set()

        def is_included(target, arr):
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        
        for num2 in nums2:
            if is_included(num2, nums1):
                intersections.add(num2)
        return list(intersections)

class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersections = set()
        nums1.sort()
        nums2.sort()
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersections.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(intersections)
