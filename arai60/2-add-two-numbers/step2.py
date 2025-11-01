class RecursiveSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_node_val(node):
            if node is None:
                return 0
            return node.val
        def get_next_node(node):
            if node is None:
                return None
            return node.next
        def add_two_numbers(l1, l2, carry):
            if l1 is None and l2 is None and carry == 0:
                return None
            total = get_node_val(l1) + get_node_val(l2) + carry
            node = ListNode(total % 10)
            node.next = add_two_numbers(get_next_node(l1), get_next_node(l2), total // 10)
            return node
        return add_two_numbers(l1, l2, 0)

class SolutionUsingNumberList:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_two_numbers(nodes: list[ListNode]):
            sentinel = ListNode()
            current = sentinel
            carry = 0

            while True:
                nodes = [node for node in nodes if node is not None]
                if not nodes and carry == 0:
                    return sentinel.next
                total = carry
                for i in range(len(nodes)):
                    node = nodes[i]
                    total += node.val
                    nodes[i] = node.next
                current.next = ListNode(total % 10)
                current = current.next
                carry = total // 10
        return add_two_numbers([l1, l2])
