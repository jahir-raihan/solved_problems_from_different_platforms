# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head):
        lst = []
        ln = -1

        while head:
            lst.append(head)
            head = head.next
            ln += 1
        root = lst.pop()

        for i in range(ln - 1, -1, -1):
            val = lst[i]

            if val.val >= root.val:
                val.next = root
                root = val
        return root


import yfinance as yf
yf.download()
