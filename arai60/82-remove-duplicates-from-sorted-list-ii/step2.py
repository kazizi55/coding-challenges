class SolutionWithHandOver:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        previous = dummy
        current = head
        value_to_skip = None

        while current is not None:
            if value_to_skip == current.val:
                current = current.next
                continue
            if current.next is not None and current.val == current.next.val:
                value_to_skip = current.val
                continue
            previous.next = current
            previous = previous.next
            current = current.next
        previous.next = None
        return dummy.next

class SolutionWithFunction:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def skipDuplicates(node, value_to_skip):
            while node is not None and node.val == value_to_skip:
                node = node.next
            return node

        dummy = ListNode()
        dummy.next = head
        previous = dummy
        current = head

        while current is not None:
            if current.next is not None and current.val == current.next.val:
                current = skipDuplicates(current.next, current.val)
                continue
            previous.next = current
            previous = previous.next
            current = current.next
        previous.next = None
        return dummy.next
