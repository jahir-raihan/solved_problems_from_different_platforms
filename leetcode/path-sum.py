# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.found = False

    def traverse(self, root, s, t):
        if root is None:
            return
        if root.val + s == t and (root.left is None) and (root.right is None):
            self.found = True
            return
        self.traverse(root.left, root.val + s, t)
        self.traverse(root.right, root.val + s, t)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        self.traverse(root, 0, targetSum)
        return self.found