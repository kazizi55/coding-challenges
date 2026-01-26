# 通らない
class InitialSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level_order = []
        queue = deque([(root.left, root.right)])
        while queue:
            order = []
            next_queue = []
            left_node, right_node = queue.popleft()
            if left_node is not None:
                order.append(left_node.val)
                next_queue.append(left_node)
            if right_node is not None:
                order.append(right_node.val)
                next_queue.append(right_node)
            level_order.append(order)
            queue = deque(next_queue)
        return level_order

class RevisedSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level)
        return result
