class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node = head
        node_vals = []
        while node is not None:
            node_vals.append(node.val)
            node = node.next
        new_head_val = node_vals.pop()
        new_head = ListNode(new_head_val)
        node = new_head
        while len(node_vals) > 0:
            node_val = node_vals.pop()
            node.next = ListNode(node_val)
            node = node.next
        return new_head