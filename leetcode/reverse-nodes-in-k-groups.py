# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        segments = [[]]

        i = 0
        s = 0
        while head:
            if i % k == 0:
                segments.append([head])
                s += 1
            else:
                segments[s].append(head)
            head = head.next
            i += 1
        for seg in segments:

            if len(seg) == k:
                for j in range(k - 1, -1, -1):
                    if j == 0:
                        seg[j].next = None
                    else:
                        seg[j].next = seg[j - 1]
        for i in range(1, len(segments) - 1):
            if len(segments[i + 1]) == k:
                segments[i][0].next = segments[i + 1][-1]
            else:
                segments[i][0].next = segments[i + 1][0]

        return segments[1][-1]

