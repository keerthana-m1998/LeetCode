# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        # 1 : find len of LL 'n'
        tail = head
        n = 1
        while tail.next:
            tail = tail.next # at last node
            n+=1
        # 2 effectice K
        k = k%n
        if k == 0:
            return head # No rotation needed
        
        # FInd beak point and new head (n-k-1 , n-k)
        new_tail = head
        for _ in range(n-k-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        tail.next = head
        return new_head

        