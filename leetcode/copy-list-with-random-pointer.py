class Solution:

    def __int__(self):
        self.vis = {}

    def copyRandomList(self, head):

        if not head:
            return None

        if head in self.vis:
            return self.vis[head]

        new = Node(head.val)
        self.vis[head] = new

        new.next = self.copyRandomList(head.next)
        new.random = self.copyRandomList(head.random)

        return new