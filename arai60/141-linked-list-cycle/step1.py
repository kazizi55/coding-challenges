class InitialSolution:
    # MEMO: 途中までしか書けませんでした
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        traversed = []
        while true:

class RevisedSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        current_node = head

        while current_node != None:
            if current_node in visited_nodes:
                return True
            else:
                visited_nodes.add(current_node)
                current_node = current_node.next
        
        return False
    
# MEMO: Floyd's Tortoise and Hare Algorithm を使用
class AnotherSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                return True
        
        return False
