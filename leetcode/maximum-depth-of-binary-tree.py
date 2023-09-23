# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def get_depth(self, root, n):
        if root is None:
            return n

        return max(self.get_depth(root.left, n + 1), self.get_depth(root.right, n + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_depth(root, 0)
