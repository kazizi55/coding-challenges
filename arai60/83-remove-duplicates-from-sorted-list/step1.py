# WA 11 / 168 testcases passed
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_vals = set()
        sentinel = ListNode()
        sentinel.next = head
        node = sentinel
        while node.next is not None:
            if node.next.val in node_vals:
                node.next = node.next.next
                continue
            node_vals.add(node.val)
            node = node.next
        return head

class RevisedSolution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None and node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
                continue
            node = node.next
        return head

class RevisedSolutionWithRecursion:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def remove_duplicates(node) -> Optional[ListNode]:
            if node is None or node.next is None:
                return node
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            remove_duplicates(node.next)
            return node
        return remove_duplicates(head)

class SolutionNotBreakingInput:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node = head
        new_head = ListNode(head.val)
        new_node = new_head
        while node is not None and node.next is not None:
            if node.val != node.next.val:
                new_node.next = ListNode(node.next.val)
                new_node = new_node.next
            node = node.next
        return new_head

class RevisedSolutionReversingCondition:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None and node.next is not None:
            if node.val != node.next.val:
                node = node.next
                continue
            node.next = node.next.next
        return head