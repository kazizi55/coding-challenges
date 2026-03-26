class Solution1:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if root is None:
            return [None, None]
        if root.val <= target:
            smaller_child_node, larger_child_node = self.splitBST(root.right, target)
            root.right = smaller_child_node
            return [root, larger_child_node]
        smaller_child_node, larger_child_node = self.splitBST(root.left, target)
        root.left = larger_child_node
        return [smaller_child_node, root]

class Solution2:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if root is None:
            return [None, None]
        smaller_sentinel = TreeNode()
        smaller = smaller_sentinel
        larger_sentinel = TreeNode()
        larger = larger_sentinel
        while root is not None:
            if root.val <= target:
                smaller.right = root
                smaller = smaller.right
                root = root.right
                smaller.right = None
                continue
            larger.left = root
            larger = larger.left
            root = root.left
            larger.left = None
        return [smaller_sentinel.right, larger_sentinel.left]
