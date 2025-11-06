# NOTE: 通らない
class InitialSolution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        new_head = ListNode(head.val)
        new_node = new_head

        while node is not None and node.next is not None:
            if node.val == node.next.val:
                node = node.next.next
                continue
            node = node.next
            new_node.next = ListNode(node.val)
            new_node = new_node.next
        return new_head

class RevisedSolution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        previous = dummy
        current = head

        while current is not None and current.next is not None:
            if current.val != current.next.val:
                previous = current
                current = current.next
                continue
            value_to_remove = current.val
            while current is not None and current.val == value_to_remove:
                current = current.next
            previous.next = current
        return dummy.next
