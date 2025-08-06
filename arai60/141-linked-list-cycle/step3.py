class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        node = head

        while node != None:
            if node in visited_nodes:
                return True
            else:
                visited_nodes.add(node)
                node = node.next
        
        return False
    
# MEMO: Solution1と同じ
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        node = head

        while node != None:
            if node in visited_nodes:
                return True
            else:
                visited_nodes.add(node)
                node = node.next
        
        return False

class Solution3:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # MEMO: 問題文に「reach」という表現があったので使用
        reached_nodes = set()
        node = head

        while node != None:
            if node in reached_nodes:
                return True
            else:
                reached_nodes.add(node)
                node = node.next
        
        return False