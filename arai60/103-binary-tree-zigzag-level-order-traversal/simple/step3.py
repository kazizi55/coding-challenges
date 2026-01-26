class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes_in_depth = [root]
        node_values = []
        depth = 1
        while nodes_in_depth:
            nodes_in_next_depth = []
            node_values_in_depth = []
            for node in nodes_in_depth:
                node_values_in_depth.append(node.val)
                if node.left is not None:
                    nodes_in_next_depth.append(node.left)
                if node.right is not None:
                    nodes_in_next_depth.append(node.right)
            if depth % 2 == 0:
                node_values.append(node_values_in_depth[::-1])
            else:
                node_values.append(node_values_in_depth)
            nodes_in_depth = nodes_in_next_depth
            depth += 1
        return node_values
