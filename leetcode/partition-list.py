# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_then = []
        grater_then = []

        while head:
            if head.val < x:
                less_then.append(head)
            else:
                grater_then.append(head)

            head = head.next

        final_lst = less_then + grater_then + [None]

        for i in range(len(final_lst) - 1):
            final_lst[i].next = final_lst[i + 1]

        return final_lst[0]