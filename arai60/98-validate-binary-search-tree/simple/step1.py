# 77 / 86 testcases passed
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = deque([root])
        while nodes:
            for _ in range(len(nodes)):
                node = nodes.popleft()
                if node.left is not None:
                    if node.left.val >= node.val:
                        return False
                    nodes.append(node.left)
                if node.right is not None:
                    if node.right.val <= node.val:
                        return False
                    nodes.append(node.right)
        return True
