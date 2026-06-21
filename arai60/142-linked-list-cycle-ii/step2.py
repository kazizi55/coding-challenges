class SetSolutionWithRecursion:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()

        def check_node(node):
            if node is None:
                return None
            
            if node in visited:
                return node

            visited.add(node)
            return check_node(node.next)
        
        return check_node(head)

class HareAndTortoiseSolutionWithFunction:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_catchup_node(node):
            slow = node
            fast = node

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

                if slow is fast:
                    return slow
            
            return None
        
        catchup_node = get_catchup_node(head)

        if catchup_node is None:
            return None
        
        finder = head

        while finder is not catchup_node:
            finder = finder.next
            catchup_node = catchup_node.next
        
        return finder

class HareAndTortoiseSolutionWithInfiniteLoop:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while True:
            if fast is None or fast.next is None:
                return None
            
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        
        finder = head
        while finder is not fast:
            finder = finder.next
            fast = fast.next
        
        return finder
