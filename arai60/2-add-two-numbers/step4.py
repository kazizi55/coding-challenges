# divmod 関数を使う version
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_node_val(node):
            if node is None:
                return 0
            return node.val
        
        sentinel = ListNode()
        node = sentinel
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            total = get_node_val(l1) + get_node_val(l2) + carry
            carry, next_val = divmod(total, 10)
            node.next = ListNode(next_val)
            node = node.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return sentinel.next

# 番兵を使わず、代わりにwhileループ内に条件分岐を作る version
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_node_val(node):
            if node is None:
                return 0
            return node.val
        
        head = None
        tail = None
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            total = get_node_val(l1) + get_node_val(l2) + carry
            carry = total // 10
            node = ListNode(total % 10)
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return head

# SolutionUsingNumberList を while nodes or carry != 0 で書き直した version
class Solution3:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def _addTwoNumbers(nodes: list[ListNode]):
            sentinel = ListNode()
            current = sentinel
            carry = 0
            nodes = [node for node in nodes if node is not None]
            while nodes or carry != 0:
                total = carry
                next_nodes = []
                for node in nodes:
                    total += node.val
                    if node.next is not None:
                        next_nodes.append(node.next)
                current.next = ListNode(total % 10)
                current = current.next
                carry = total // 10
                nodes = next_nodes
            return sentinel.next
                
        return _addTwoNumbers([l1, l2])

# val の total への加算と next へ進めることをまとめる version
class Solution4:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        node = sentinel
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            total = carry
            if l1 is not None:
                total += l1.val
                l1 = l1.next
            if l2 is not None:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            node.next = ListNode(total % 10)
            node = node.next
        return sentinel.next
