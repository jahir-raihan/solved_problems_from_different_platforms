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
        self.lst.append(root.val)
        self.traverse(root.right)
        self.traverse(root.left)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root)
        self.lst.sort()
        return self.lst[k-1]