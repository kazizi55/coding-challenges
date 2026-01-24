class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def index_to_BST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left = index_to_BST(left, middle - 1)
            root.right = index_to_BST(middle + 1, right)
            return root
        return index_to_BST(0, len(nums) -1)

class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def index_range_to_bst(left: int, right: int) -> Optional[TreeNode]:
            if left >= right:
                return None
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left = index_range_to_bst(left, middle)
            root.right = index_range_to_bst(middle + 1, right)
            return root
        return index_range_to_bst(0, len(nums))
