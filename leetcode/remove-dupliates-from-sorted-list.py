# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        res = []

        while head:
            if not ((prev and prev.val == head.val) or (head.next and head.next.val == head.val)):
                res.append(head)
            prev = head
            head = head.next
        if not res:
            return None
        root = res[0]
        for i in range(len(res) - 1):
            res[i].next = res[i + 1]
        res[-1].next = None
        return root