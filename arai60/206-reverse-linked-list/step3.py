class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(node):
            if node is None:
                return None, None
            if node.next is None:
                return node, node
            next_node = node.next
            head, tail = reverse_list_helper(next_node)
            tail.next = node
            node.next = None
            return head, node
        node, _ = reverse_list_helper(head)
        return node

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(reversed, rest):
            if rest is None:
                return reversed
            next_node = rest.next
            rest.next = reversed
            return reverse_list_helper(rest, next_node)
        return reverse_list_helper(None, head)

class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(node):
            if node is None:
                return None, None
            if node.next is None:
                return node, node
            next_node = node.next
            head, tail = reverse_list_helper(next_node)
            tail.next = node
            node.next = None
            return head, node
        node, _ = reverse_list_helper(head)
        return node
