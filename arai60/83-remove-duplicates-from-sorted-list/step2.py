class SolutionWithDoubledLoop:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None:
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head

class SolutionWithANewLinkedList:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node = head
        new_head = ListNode(head.val)
        new_node = new_head

        while node is not None and node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
                continue
            node = node.next
            added_node = ListNode(node.val)
            new_node.next = added_node
            new_node = added_node
        return new_head
