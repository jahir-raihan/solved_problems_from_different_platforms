# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.levels = {}

    def traverse(self, root, level):
        if root is None:
            if level in self.levels:
                self.levels[level].append(root)
            else:
                self.levels[level] = [root]
            return

        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)

        if level in self.levels:
            self.levels[level].append(root.val)
        else:
            self.levels[level] = [root.val]

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        self.traverse(root, 0)

        for k, v in self.levels.items():

            i, j = 0, len(v) - 1
            while i < j:
                if v[i] != v[j]:
                    return False
                i += 1
                j -= 1
        return True