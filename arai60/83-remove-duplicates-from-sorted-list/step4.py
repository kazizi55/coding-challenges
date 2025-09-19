class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node = head
        new_head = ListNode(head.val)
        new_node = new_head

        while node is not None and node.next is not None:
            if node.val != node.next.val:
                new_node.next = ListNode(node.next.val)
                new_node = new_node.next
            node = node.next
        return new_head
