# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.lst = []

    def traverse(self, root):
        if root is None:
            return

        self.lst.append(root)
        self.traverse(root.left)
        self.traverse(root.right)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        self.traverse(root)

        for i in self.lst[1:]:
            root.right = i
            root.left = None
            root = root.right

        return self.lst[0]