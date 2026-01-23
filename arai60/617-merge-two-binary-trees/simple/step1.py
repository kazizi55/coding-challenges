# 途中まで。
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        merged = None
        node1 = root1
        node2 = root2
        while node1 is not None or node2 is not None:
            if node1 is not None and node2 is not None:
                node = TreeNode(node1.val + node2.val)
