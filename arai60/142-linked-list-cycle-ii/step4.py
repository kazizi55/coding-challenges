class SetSolutionWithArgument:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_node(node, visited):
            if node is None:
                return None
            if node in visited:
                return node
            visited.add(node)

            return find_node(node.next, visited)
        return find_node(head, set())

class SetSolution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        node = head

        while node is not None:
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return None

class HareAndTortoise:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_intersection(node):
            slow = node
            fast = node

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return slow
            return None
        
        node_from_intersection = find_intersection(head)
        if node_from_intersection is None:
            return None
        
        node_from_head = head
        while node_from_head is not node_from_intersection:
            node_from_head = node_from_head.next
            node_from_intersection = node_from_intersection.next
        return node_from_head
