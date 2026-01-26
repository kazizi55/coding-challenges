# 14 / 33 testcases passed
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes = deque([root])
        node_values = []
        is_left_to_right = True
        while nodes:
            node_values_in_depth = []
            is_left_to_right = not is_left_to_right
            for _ in range(len(nodes)):
                node = nodes.popleft()
                node_values_in_depth.append(node.val)
                if is_left_to_right and node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
                if not is_left_to_right and node.left is not None:
                    nodes.append(node.left)
            node_values.append(node_values_in_depth)
        return node_values

class RevisedSolution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes = deque([root])
        node_values = []
        is_left_to_right = True
        while nodes:
            node_values_in_depth = []
            for _ in range(len(nodes)):
                node = nodes.popleft()
                node_values_in_depth.append(node.val)
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
            if is_left_to_right:
                node_values.append(node_values_in_depth)
            else:
                node_values.append(node_values_in_depth[::-1])
            is_left_to_right = not is_left_to_right
        return node_values
