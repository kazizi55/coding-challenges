class Solution:
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
                continue
            tail.next = node
            tail = tail.next
            node = node.next
        return sentinel.next