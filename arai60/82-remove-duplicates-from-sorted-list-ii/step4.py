class SolutionWithSeparationAndHandOver:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        previous = dummy
        current = head
        val_to_remove = None

        while current is not None:
            if current.val == val_to_remove:
                current = current.next
                continue
            
            if current.next is not None and current.val == current.next.val:
                val_to_remove = current.val
                previous.next = None
                current = current.next
                continue
            previous.next = current
            previous = previous.next
            current = current.next
        return dummy.next
    
class SolutionWithoutValueToSkip:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        previous = dummy
        current = head

        while current is not None:            
            if current.next is not None and current.val == current.next.val:
                while current.next is not None and current.val == current.next.val:
                    current = current.next
                current = current.next
                continue    
            previous.next = current
            previous = previous.next
            current = current.next
        previous.next = None
        return dummy.next
	
class SolutionWithMoveToDistinctNode:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def moveToNextDistinctNode(node: Optional[ListNode], val_to_skip: int) -> ListNode:
            while node is not None and node.val == val_to_skip:
                node = node.next
            return node
        dummy = ListNode()
        dummy.next = head
        previous = dummy
        current = head

        while current is not None:
            if current.next is not None and current.val == current.next.val:
                current = moveToNextDistinctNode(current.next, current.val)
                previous.next = None
                continue
            previous.next = current
            previous = previous.next
            current = current.next
        return dummy.next

class SolutionWithClearVariableNames:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def moveToDistinctNode(node: Optional[ListNode], val_to_skip: int) -> ListNode:
            while node is not None and node.val == val_to_skip:
                node = node.next
            return node
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        node = head

        while node is not None:
            if node.next is not None and node.val == node.next.val:
                node = moveToDistinctNode(node.next, node.val)
                tail.next = None
                continue
            tail.next = node
            tail = tail.next
            node = node.next
        return dummy.next
