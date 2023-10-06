class Solution:
    def __init__(self):
        self.values = []

    def traverse(self, root):

        if root is None:
            return
        self.values.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)

        self.values.sort()
        min_diff = 9999999999
        for i in range(1, len(self.values)):
            min_diff = min(min_diff, self.values[i] - self.values[i - 1])
        return min_diff