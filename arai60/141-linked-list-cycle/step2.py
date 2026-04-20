class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # MEMO: == はオブジェクトが持つデータが同じかをチェック、is はオブジェクトそのものが同じか (メモリ上の同じオブジェクトを指しているか)をチェック
            # SEE:  https://github.com/ryosuketc/leetcode_arai60/pull/1#discussion_r2083814842
            if (slow is fast): 
                return True
        
        return False

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()

        # MEMO: current_node を node にリネーム
        node = head

        while node != None:
            if node in visited_nodes:
                return True
            else:
                visited_nodes.add(node)
                node = node.next
        
        return False
