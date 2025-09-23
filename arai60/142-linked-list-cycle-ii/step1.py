class InitialSolution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        node = head

        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        
        return None
        
# MEMO: Hare and Tortoise で解いてみたが、5分以内にACにならなかった
class HareAndTortoiseInitialSolution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return fast
        
        return None
  
class HareAndTortoiseRevisedSolution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            return None
        
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        
        return slow
