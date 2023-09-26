# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def traverse(self, root, p):
        if root is None:
            return

        if root.right is None and root.left is None:
            val = int(p + str(root.val))
            self.sum += val
            return
        self.traverse(root.left, p + str(root.val))
        self.traverse(root.right, p + str(root.val))

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, '')
        return self.sum