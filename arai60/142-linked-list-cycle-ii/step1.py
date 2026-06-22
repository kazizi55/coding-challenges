class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return None

class SolutionWithRecursion:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_node(node, visited) -> Optional[ListNode]:
            if node is None:
                return None
            if node in visited:
                return node
            visited.add(node)
            return find_node(node.next, visited)
        return find_node(head, set())

class SolutionWithTortoiseAndHare:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_intersection_node(fast, slow) -> Optional[ListNode]:
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return slow
            return None

        intersection_node = find_intersection_node(head, head)
        if intersection_node is None:
            return None
        node = head
        while node is not intersection_node:
            node = node.next
            intersection_node = intersection_node.next
        return node