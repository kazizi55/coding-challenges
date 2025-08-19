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
        def find_catchup_node(node):
            slow = node
            fast = node

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

                if slow is fast:
                    return slow
                
            return None
        
        catchup_node = find_catchup_node(head)

        if catchup_node is None:
            return None
        
        finder = head

        while finder is not catchup_node:
            finder = finder.next
            catchup_node = catchup_node.next
        
        return finder