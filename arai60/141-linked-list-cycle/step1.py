class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast is not None:
            if fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False