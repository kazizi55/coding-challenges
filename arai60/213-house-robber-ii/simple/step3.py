class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)
        nums_without_end = nums[:-1]
        max_amount_nums_without_end = [0] * len(nums_without_end)
        max_amount_nums_without_end[0] = nums_without_end[0]
        max_amount_nums_without_end[1] = max(
            max_amount_nums_without_end[0],
            nums_without_end[1]
        )
        for i in range(2, len(nums_without_end)):
            max_amount_nums_without_end[i] = max(
                max_amount_nums_without_end[i-2] + nums_without_end[i],
                max_amount_nums_without_end[i-1]
            )
        nums_without_start = nums[1:]
        max_amount_nums_without_start = [0] * len(nums_without_start)
        max_amount_nums_without_start[0] = nums_without_start[0]
        max_amount_nums_without_start[1] = max(
            max_amount_nums_without_start[0],
            nums_without_start[1]
        )
        for i in range(2, len(nums_without_start)):
            max_amount_nums_without_start[i] = max(
                max_amount_nums_without_start[i-2] + nums_without_start[i],
                max_amount_nums_without_start[i-1]
            )
        return max(
            max_amount_nums_without_end[-1],
            max_amount_nums_without_start[-1]
        )

class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return max(nums, default=0)
        nums_without_tail = nums[:len(nums)-1]
        @cache
        def get_max_amount_without_tail(i: int) -> int:
            if i == 0:
                return nums_without_tail[0]
            if i == 1:
                return max(nums_without_tail[0], nums_without_tail[1])
            return max(get_max_amount_without_tail(i-2) + nums_without_tail[i], get_max_amount_without_tail(i-1))
        nums_without_init = nums[1:]
        @cache
        def get_max_amount_without_init(i: int) -> int:
            if i == 0:
                return nums_without_init[0]
            if i == 1:
                return max(nums_without_init[0], nums_without_init[1])
            return max(get_max_amount_without_init(i-2) + nums_without_init[i], get_max_amount_without_init(i-1))
        return max(get_max_amount_without_tail(len(nums_without_tail)-1), get_max_amount_without_init(len(nums_without_init)-1))

class Solution3:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return max(nums, default=0)
        @cache
        def get_max_amount(i: int, nums_: tuple) -> int:
            if i == 0:
                return nums_[0]
            if i == 1:
                return max(nums_[0], nums_[1])
            return max(
                get_max_amount(i-2, nums_) + nums_[i],
                get_max_amount(i-1, nums_)
            )
        nums_without_end = nums[:-1]
        nums_without_begin = nums[1:]
        return max(
            get_max_amount(len(nums_without_end)-1, tuple(nums_without_end)),
            get_max_amount(len(nums_without_begin)-1, tuple(nums_without_begin))
        )
        
class Solution4:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return max(nums, default=0)
        @cache
        def get_max_amount(begin: int, end: int) -> int:
            length = end - begin
            if length == 1:
                return nums[begin]
            if length == 2:
                return max(nums[begin], nums[begin+1])
            return max(
                nums[end-1] + get_max_amount(begin, end-2),
                get_max_amount(begin, end-1)
            )
        return max(
            get_max_amount(0, len(nums)-1),
            get_max_amount(1, len(nums))
        )
