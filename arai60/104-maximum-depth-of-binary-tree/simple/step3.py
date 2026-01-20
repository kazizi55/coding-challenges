class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        if node is None:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nodes_in_depth = [root]
        depth = 0
        while nodes_in_depth:
            depth += 1
            nodes_in_next_depth = []
            for node in nodes_in_depth:
                if node.left is not None:
                    nodes_in_next_depth.append(node.left)
                if node.right is not None:
                    nodes_in_next_depth.append(node.right)
            nodes_in_depth = nodes_in_next_depth
        return depth
