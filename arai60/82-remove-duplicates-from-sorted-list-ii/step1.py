# Wrong Answer 8 / 166 testcases passed
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(sys.maxsize)
        sentinel.next = head
        node = sentinel
        while node is not None and node.next is not None:
            if node.val == node.next.val:
                node = node.next.next
                continue
            node = node.next
        return sentinel.next

class SolutionWithValToRemove:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        tail = sentinel
        node = head
        val_to_remove = None
        while node is not None:
            if node.val == val_to_remove:
                node = node.next
                continue
            if node.next is not None and node.val == node.next.val:
                val_to_remove = node.val
                tail.next = None
                node = node.next
                continue
            tail.next = node
            tail = tail.next
            node = node.next
        return sentinel.next

class SolutionWithValToRemoveFunction:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def moved_to_next_distinct_node(current: Optional[ListNode], val_to_remove: int) -> Optional[ListNode]:
            while current is not None and current.val == val_to_remove:
                current = current.next
            return current
        
        sentinel = ListNode()
        sentinel.next = head
        tail = sentinel
        node = head
        while node is not None:
            if node.next is not None and node.val == node.next.val:
                node = moved_to_next_distinct_node(node, node.next.val)
                tail.next = node
                continue
            tail.next = node
            tail = tail.next
            node = node.next
        return sentinel.next