class Solution:
    def __init__(self):
        self.levels = {}

    def traverse(self, root, level):
        if root is None:
            return

        if level in self.levels:
            self.levels[level].append(root.val)
        else:
            self.levels[level] = [root.val]
        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0)

        res = [v for k, v in self.levels.items()]
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        return res