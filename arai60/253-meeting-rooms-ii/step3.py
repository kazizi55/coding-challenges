class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        events.sort()
        current_active_room_num = 0
        min_room_num = 0
        for _, rise_or_down in events:
            current_active_room_num += rise_or_down
            if current_active_room_num > min_room_num:
                min_room_num = current_active_room_num
        return min_room_num
