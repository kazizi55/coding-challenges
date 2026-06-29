class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node_vals = []
        node = head
        while node is not None:
            node_vals.append(node.val)
            node = node.next
        new_head_val = node_vals.pop()
        new_head = ListNode(new_head_val)
        new_node = new_head
        while len(node_vals) > 0:
            new_node_val = node_vals.pop()
            new_node.next = ListNode(new_node_val)
            new_node = new_node.next
        return new_head

class RecursiveSolutionWithTail:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(node: Optional[ListNode]) -> Tuple[Optional[ListNode], Optional[ListNode]]:
            if node is None:
                return None, None
            if node.next is None:
                return node, node
            reversed_head, tail = reverse_list_helper(node.next)
            tail.next = node
            node.next = None
            return reversed_head, node

        reversed_head, _ = reverse_list_helper(head)
        return reversed_head

class RecursiveSolutionWithoutTail:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return None
            if node.next is None:
                return node
            reversed_head = reverse_list_helper(node.next)
            node.next.next = node
            node.next = None
            return reversed_head
        return reverse_list_helper(head)

class RecursiveSolutionWithRestAndNextNode:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(reversed_head: Optional[ListNode], rest: Optional[ListNode]) -> Optional[ListNode]:
            if rest is None:
                return reversed_head
            next_node = rest.next
            rest.next = reversed_head
            return reverse_list_helper(rest, next_node)

        return reverse_list_helper(None, head)