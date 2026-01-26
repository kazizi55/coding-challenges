class Solution1:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        node_values = []
        nodes_in_depth = [root]
        while nodes_in_depth:
            node_values_in_depth = []
            nodes_in_next_depth = []
            for node in nodes_in_depth:
                node_values_in_depth.append(node.val)
                if node.left is not None:
                    nodes_in_next_depth.append(node.left)
                if node.right is not None:
                    nodes_in_next_depth.append(node.right)
            node_values.append(node_values_in_depth)
            nodes_in_depth = nodes_in_next_depth
        return node_values

class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes = deque([root])
        node_values = []
        while nodes:
            node_values_in_depth = []
            for _ in range(len(nodes)):
                node = nodes.popleft()
                node_values_in_depth.append(node.val)
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
            node_values.append(node_values_in_depth)
        return node_values
