# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        ret_root = None
        prev_root = None
        prev = None
        curr = head
        while curr:
            if prev is None:
                prev = curr
                curr = curr.next
                if curr is not None:
                    prev.next, curr.next = curr.next, prev
                    if prev_root is None:
                        prev_root = prev
                    else:
                        prev_root.next = curr
                        prev_root = prev
                    if ret_root is None:
                        ret_root = curr
                    curr = prev.next
                    prev = None
                else:
                    break
        if ret_root is None:
            return head
        else:
            return ret_root
