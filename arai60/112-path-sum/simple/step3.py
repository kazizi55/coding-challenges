class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_valid_path(node, total):
            if node is None:
                return False
            total += node.val
            if node.left is None and node.right is None:
                return targetSum == total
            return is_valid_path(node.left, total) or is_valid_path(node.right, total)
        return is_valid_path(root, 0)
