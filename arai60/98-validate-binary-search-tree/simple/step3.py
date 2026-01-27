class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_from_range(node: Optional[TreeNode], high: int, low: int) -> bool:
            if node is None:
                return True
            if not(low < node.val < high):
                return False
            return is_valid_from_range(node.left, node.val, low) and is_valid_from_range(node.right, high, node.val)
        MAX_VALUE = sys.maxsize
        MIN_VALUE = -sys.maxsize
        return is_valid_from_range(root, MAX_VALUE, MIN_VALUE)

class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        MIN_VALUE = -sys.maxsize
        MAX_VALUE = sys.maxsize
        node_stack = [(root, MIN_VALUE, MAX_VALUE)]
        while node_stack:
            node, low, high = node_stack.pop()
            if not(low < node.val < high):
                return False
            if node.left is not None:
                node_stack.append((node.left, low, node.val))
            if node.right is not None:
                node_stack.append((node.right, node.val, high))
        return True

class Solution3:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        MIN_VALUE = -sys.maxsize
        MAX_VALUE = sys.maxsize
        node_queue = deque([(root, MIN_VALUE, MAX_VALUE)])
        while node_queue:
            node, low, high = node_queue.popleft()
            if not(low < node.val < high):
                return False
            if node.left is not None:
                node_queue.append((node.left, low, node.val))
            if node.right is not None:
                node_queue.append((node.right, node.val, high))
        return True

class Solution4:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_node_val = -math.inf
        def is_valid_BST(node):
            nonlocal min_node_val
            if node is None:
                return True
            if not is_valid_BST(node.left):
                return False
            if min_node_val >= node.val:
                return False
            min_node_val = node.val
            if not is_valid_BST(node.right):
                return False
            return True
        return is_valid_BST(root)
