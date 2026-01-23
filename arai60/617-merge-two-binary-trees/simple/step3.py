class Solution1:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        new_root = TreeNode(root1.val + root2.val)
        new_root.left = self.mergeTrees(root1.left, root2.left)
        new_root.right = self.mergeTrees(root1.right, root2.right)
        return new_root

class Solution2:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return TreeNode(root2.val, root2.left, root2.right)
        if root2 is None:
            return TreeNode(root1.val, root1.left, root1.right)
        new_node = TreeNode(root1.val + root2.val)
        new_node.left = self.mergeTrees(root1.left, root2.left)
        new_node.right = self.mergeTrees(root1.right, root2.right)
        return new_node

class Solution3:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

class Solution4:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        stack = [(root1, root2)]
        while stack:
            node1, node2 = stack.pop()
            node1.val += node2.val
            if node1.left is not None and node2.left is not None:
                stack.append((node1.left, node2.left))
            if node1.left is None:
                node1.left = node2.left
            if node1.right is not None and node2.right is not None:
                stack.append((node1.right, node2.right))
            if node1.right is None:
                node1.right = node2.right
        return root1

class Solution5:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        queue = deque([(root1, root2)])
        while queue:
            node1, node2 = queue.popleft()
            node1.val += node2.val
            if node1.left is not None and node2.left is not None:
                queue.append((node1.left, node2.left))
            if node1.left is None:
                node1.left = node2.left
            if node1.right is not None and node2.right is not None:
                queue.append((node1.right, node2.right))
            if node1.right is None:
                node1.right = node2.right
        return root1
