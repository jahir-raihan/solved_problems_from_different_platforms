class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.in_order = [-1]
        self.i = 0
        self.traverse(root)
        print(self.in_order)

    def traverse(self, root):
        if root is None:
            return

        self.traverse(root.left)
        self.in_order.append(root.val)
        self.traverse(root.right)

    def next(self) -> int:
        self.i += 1
        return self.in_order[self.i]

    def hasNext(self) -> bool:
        return True if self.i < len(self.in_order) - 1 else False