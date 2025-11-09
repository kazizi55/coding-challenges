# 再帰で head を上書きしない version (tail あり)
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(node):
            if node is None:
                return None, None
            if node.next is None:
                return node, node
            next_node = node.next
            reversed_head, tail = reverse_list_helper(next_node)
            tail.next = node
            node.next = None
            return reversed_head, node

        reversed_head, _ = reverse_list_helper(head)
        return reversed_head

# 再帰で head を上書きしない version (tail なし)
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(node):
            if node is None:
                return None
            if node.next is None:
                return node
            next_node = node.next
            reversed_head = reverse_list_helper(next_node)
            node.next.next = node
            node.next = None
            return reversed_head
        reversed_head = reverse_list_helper(head)
        return reversed_head

# stack を使う version (while stack でループを回す)
class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []
        while node is not None:
            stack.append(node.val)
            node = node.next
        sentinel = ListNode()
        node = sentinel
        while stack:
            num = stack.pop()
            node.next = ListNode(num)
            node = node.next
        return sentinel.next

# stack を使う version (for num in reversed(stack) でループを回す)
class Solution4:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []

        while node is not None:
            stack.append(node.val)
            node = node.next
        sentinel = ListNode()
        node = sentinel
        for num in reversed(stack):
            node.next = ListNode(num)
            node = node.next
        return sentinel.next

# 再帰の rest を渡す version (reversed を上書きしない)
class Solution5:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(reversed_head, rest):
            if rest is None:
                return reversed_head
            next_node = rest.next
            rest.next = reversed_head
            return reverse_list_helper(rest, next_node)

        return reverse_list_helper(None, head)
