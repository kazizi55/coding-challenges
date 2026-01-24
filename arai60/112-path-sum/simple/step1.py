# 67 / 118 testcases passed
class InitialSolution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        has_path_sum = False
        if root.left is not None:
            has_path_sum = self.hasPathSum(root.left, targetSum - root.left.val)
        if not has_path_sum and root.right is not None:
            has_path_sum = self.hasPathSum(root.right, targetSum - root.right.val)
        return has_path_sum

# AC
class RevisedSolution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        total = targetSum - root.val
        if root.left is None and root.right is None:
            return total == 0
        return self.hasPathSum(root.left, total) or self.hasPathSum(root.right, total)
