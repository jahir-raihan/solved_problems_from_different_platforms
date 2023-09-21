# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        if head is None:
            return None

        while head:
            lst.append(head)
            head = head.next

        rotate = k % len(lst)
        lst = lst[-rotate:] + lst[:-rotate] + [None]

        for i in range(len(lst) - 1):
            lst[i].next = lst[i + 1]
        return lst[0]
