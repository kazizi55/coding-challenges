class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None and node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
                continue
            node = node.next
        return head