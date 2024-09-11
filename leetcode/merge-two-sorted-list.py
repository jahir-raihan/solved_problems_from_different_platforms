# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while list1:
            values.append(list1)
            list1 = list1.next
        while list2:
            values.append(list2)
            list2 = list2.next

        nodes_list = sorted(values, key=lambda x: x.val)
        for i in range(len(nodes_list) - 1):
            nodes_list[i].next = nodes_list[i + 1]
        if nodes_list:
            nodes_list[-1].next = None
            return nodes_list[0]
