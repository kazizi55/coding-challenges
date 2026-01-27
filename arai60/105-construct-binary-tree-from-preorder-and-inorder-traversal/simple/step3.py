class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_val_to_inorder_index = {}
        for i, node_val in enumerate(inorder):
            node_val_to_inorder_index[node_val] = i
        preorder_index = 0
        def build_tree_from_inorder(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            nonlocal preorder_index
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            inorder_index = node_val_to_inorder_index[root.val]
            root.left = build_tree_from_inorder(left, inorder_index - 1)
            root.right = build_tree_from_inorder(inorder_index + 1, right)
            return root
        return build_tree_from_inorder(0, len(inorder) - 1)

class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        def build_tree_from_inorder(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            nonlocal preorder_index
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            inorder_index = inorder.index(root.val)
            root.left = build_tree_from_inorder(left, inorder_index - 1)
            root.right = build_tree_from_inorder(inorder_index + 1, right)
            return root
        return build_tree_from_inorder(0, len(inorder) - 1)
