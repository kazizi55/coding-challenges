class RevisedSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        node = head

        # MEMO: None などの singleton との比較には is not を使うようにする
        # MEMO: 条件文に括弧をつける・つけないは統一する
        while node is not None:
            if node in visited_nodes:
                return True
            else:
                visited_nodes.add(node)
                node = node.next
        
        return False