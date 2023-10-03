
class Solution:

    def __init__(self):
        self.sum = -9999999999

    def traverse(self, root):
        if root is None:
            return 0

        right_sum = max(self.traverse(root.right), 0)
        left_sum = max(self.traverse(root.left), 0)
        val = root.val + right_sum + left_sum

        self.sum = max(val, self.sum)

        return root.val + max(right_sum, left_sum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.sum
