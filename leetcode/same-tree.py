# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.lst1 = []
        self.lst2 = []

    def get_list1(self, root):
        if root is None:
            self.lst1.append(root)
            return

        self.lst1.append(root.val)

        self.get_list1(root.left)
        self.get_list1(root.right)

    def get_list2(self, root):
        if root is None:
            self.lst2.append(root)
            return

        self.lst2.append(root.val)

        self.get_list2(root.left)
        self.get_list2(root.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.get_list1(p)
        self.get_list2(q)

        return self.lst1 == self.lst2