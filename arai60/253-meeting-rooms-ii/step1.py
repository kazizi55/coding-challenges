# WA
class Solution1:
    MAX_RANGE = 10 ** 4
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_end_times = [0] * Solution.MAX_RANGE
        for start_time, end_time in intervals:
            start_end_times[start_time] += 1
            start_end_times[end_time] -= 1
        prefix_num = 0
        for index in range(len(start_end_times)):
            prefix_num += start_end_times[index]
        return prefix_num
    
# 解けず
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        last_end_time = -1
        min_room_num = 1
        for start_time, end_time in sorted_intervals:
            if start_time < last_end_time:
                min_room_num += 1
            