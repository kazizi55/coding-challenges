class Solution1:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        last_interval_end = -1
        for interval_start, interval_end in sorted_intervals:
            if interval_start < last_interval_end:
                return False
            last_interval_end = interval_end
        return True

class Solution2:
    MAX_RANGE = 10 ** 6 + 1
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start_end_times = [0] * Solution2.MAX_RANGE
        for start, end in intervals:
            start_end_times[start] += 1
            start_end_times[end] -= 1
        prefix_sum = 0
        for index in range(len(start_end_times)):
            prefix_sum += start_end_times[index]
            if prefix_sum >= 2:
                return False
        return True
