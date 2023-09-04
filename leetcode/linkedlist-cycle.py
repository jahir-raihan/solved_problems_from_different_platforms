class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vis = set()

        while head:
            if head in vis:
                return True
            vis.add(head)
            head = head.next
        return False