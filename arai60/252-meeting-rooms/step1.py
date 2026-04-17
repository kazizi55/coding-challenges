# Wrong Answer 71 / 79 testcases passed
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        can_attend = True
        max_start = sys.maxsize
        min_end = -sys.maxsize
        for index in range(len(intervals)):
            current_interval = intervals[index]
            current_interval_start = current_interval[0]
            current_interval_end = current_interval[1]
            if current_interval_start >= max_start or current_interval_end <= min_end:
                return False
            max_start = min(max_start, current_interval_start)
            min_end = max(min_end, current_interval_end)
        return can_attend

class RevisedSolution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        previous_interval_end = -sys.maxsize
        for index in range(len(intervals)):
            current_interval = intervals[index]
            current_interval_start = current_interval[0]
            current_interval_end = current_interval[1]
            if previous_interval_end > current_interval_start:
                return False
            previous_interval_end = current_interval_end
        return True
