class Solution1:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        node = root
        if node.left is None:
            return 1 + self.minDepth(node.right)
        if node.right is None:
            return 1 + self.minDepth(node.left)
        return 1 + min(self.minDepth(node.left), self.minDepth(node.right))

class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        nodes_in_depth = [root]
        while nodes_in_depth:
            nodes_in_next_depth = []
            for node in nodes_in_depth:
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    nodes_in_next_depth.append(node.left)
                if node.right is not None:
                    nodes_in_next_depth.append(node.right)
            nodes_in_depth = nodes_in_next_depth
            depth += 1
        return depth
