class InitialSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if head is None:
            return None

        stack = []
        node = head

        while node is not None:
            stack.append(node.val)
            node = node.next

        sentinel = ListNode()
        node = sentinel
        for num in stack[::-1]:
            node.next = ListNode(num)
            node = node.next
        return sentinel.next
