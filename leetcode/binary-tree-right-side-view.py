# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

        self.vis = set()

    def traverse(self, root, level):
        if root is None:
            return
        self.res.append(root.val)
        self.vis.add(level)
        self.traverse(root.right, level + 1)

    def traverse2(self, root, level):
        if root is None:
            return

        if level not in self.vis:
            self.res.append(root.val)
            self.vis.add(level)

        self.traverse2(root.right, level + 1)
        self.traverse2(root.left, level + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root, 0)
        self.traverse2(root, 0)
        return self.res

