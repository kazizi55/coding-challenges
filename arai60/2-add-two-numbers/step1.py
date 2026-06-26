# NOTE: 通らない
class InitialSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        has_carried_over = False

        while l1 is not None and l2 is not None:
            val = l1.val + l2.val

            if has_carried_over:
                val = val + 1

            if val > 9:
                has_carried_over = True
                strVal = str(val)
                val = int(strVal[-1])
            else:
                has_carried_over = False
            
            node.next = ListNode(val)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        return dummy.next

class RevisedSolution:
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
            carry = total // 10
            node.next = ListNode(total % 10)
            node = node.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return sentinel.next
