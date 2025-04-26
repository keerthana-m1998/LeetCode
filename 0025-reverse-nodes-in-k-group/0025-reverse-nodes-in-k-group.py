# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev_group_end = dummy

        while True:
            #Check if K nodes exist
            kth_node = getKthNode(prev_group_end,k)
            if not kth_node:
                break
            # Prepare for reversal
            next_group_start = kth_node.next
            prev , curr = next_group_start,prev_group_end.next

            # Reverse K nodes
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Re connect with previous node
            new_group_end = prev_group_end.next
            prev_group_end.next = prev # prev is the new group head
            prev_group_end = new_group_end

        return dummy.next


def getKthNode(node,k):
    while node and k>0:
        node = node.next
        k-=1
    return node
        