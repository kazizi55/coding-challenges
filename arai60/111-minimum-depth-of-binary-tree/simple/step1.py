class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        nodes_in_depth = [root]
        while nodes_in_depth:
            depth += 1
            nodes_in_next_depth = []
            for node in nodes_in_depth:
                if node.left is None and node.right is None:
                    nodes_in_next_depth = []
                    break
                if node.left is not None:
                    nodes_in_next_depth.append(node.left)
                if node.right is not None:
                    nodes_in_next_depth.append(node.right)
            nodes_in_depth = nodes_in_next_depth
        return depth        
