class MyHeap:
    def __init__(self, items=None):
        if items is None:
            self.min_heap = []
        else:
            self.min_heap = items
        for i in reversed(range(len(self.min_heap) // 2)):
            self._sift_down(i)

    def __len__(self):
        return len(self.min_heap)

    def push(self, item):
        self.min_heap.append(item)
        self._sift_up(len(self.min_heap) - 1)

    def pop(self):
        if len(self.min_heap) < 2:
            return self.min_heap.pop()
        last = self.min_heap.pop()
        smallest = self.min_heap[0]
        self.min_heap[0] = last
        self._sift_down(0)
        return smallest

    def top(self):
        return self.min_heap[0]

    def _sift_up(self, pos):
        item = self.min_heap[pos]
        while pos > 0:
            parent_pos = (pos - 1) >> 1
            parent_item = self.min_heap[parent_pos]
            if item >= parent_item:
                break
            self._swap_item(pos, parent_pos)
            pos = parent_pos

    def _sift_down(self, pos):
        def min_item_pos(left_child_pos, right_child_pos):
            if self.min_heap[left_child_pos] < self.min_heap[right_child_pos]:
                return left_child_pos
            else:
                return right_child_pos

        child_pos = pos * 2 + 1
        while child_pos < len(self.min_heap):
            right_child_pos = child_pos + 1
            if right_child_pos < len(self.min_heap):
                child_pos = min_item_pos(child_pos, right_child_pos)
            if self.min_heap[child_pos] >= self.min_heap[pos]:
                break
            self._swap_item(child_pos, pos)
            pos = child_pos
            child_pos = child_pos * 2 + 1

    def _swap_item(self, pos1, pos2):
        self.min_heap[pos1], self.min_heap[pos2] = (
            self.min_heap[pos2],
            self.min_heap[pos1],
        )
