class Solution1:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_loadable_capacity(capacity: int):
            required_days = 1
            prefix_load = 0
            for weight in weights:
                prefix_load += weight
                if prefix_load <= capacity:
                    continue
                prefix_load = weight
                required_days += 1
            return required_days <= days
        low = max(weights)
        high = sum(weights) + 1
        while low < high:
            middle = (low + high) // 2
            if is_loadable_capacity(middle):
                high = middle
                continue
            low = middle + 1
        return low

class Solution2:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_loadable_within_days(capacity: int):
            required_days = 1
            prefixed_weight = 0
            for weight in weights:
                prefixed_weight += weight
                if prefixed_weight <= capacity:
                    continue
                prefixed_weight = weight
                required_days += 1
            return required_days <= days
        return bisect_left(range(sum(weights) + 1), True, lo=max(weights), key=is_loadable_within_days)
