class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        node_list = []

        while head:
            node_list.append(head.val)
            head = head.next

        node_list[left - 1:right] = node_list[left - 1:right][::-1]

        root = ListNode(node_list[0])
        tmp_root = root

        for i in range(1, len(node_list)):
            tmp_root.next = ListNode(node_list[i])
            tmp_root = tmp_root.next
        return root