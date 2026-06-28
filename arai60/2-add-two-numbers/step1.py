class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        node = sentinel
        is_carried_over = False
        while l1 is not None or l2 is not None:
            l1_val = 0
            l2_val = 0
            if l1 is not None:
                l1_val = l1.val
                l1 = l1.next
            if l2 is not None:
                l2_val = l2.val
                l2 = l2.next
            total = l1_val + l2_val
            if is_carried_over == True:
                total += 1
            if total > 9:
                total -= 10
                is_carried_over = True
            else:
                is_carried_over = False
            node.next = ListNode(total)
            node = node.next
        if is_carried_over == True:
            node.next = ListNode(1)
        return sentinel.next

class SolutionWithSeparatedFunction:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_node_val(node: Optional[ListNode]) -> int:
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

class SolutionWithoutSentinel:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_node_val(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return 0
            return node.val

        head = None
        tail = None
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            total = get_node_val(l1) + get_node_val(l2) + carry
            carry = total // 10
            next_val = total % 10
            node = ListNode(next_val)
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

class SolutionAddingUpTotalInOneDirection:
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
            next_val = total % 10
            node.next = ListNode(next_val)
            node = node.next
        return sentinel.next