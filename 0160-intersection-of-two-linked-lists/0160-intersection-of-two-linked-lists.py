# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Two pointers O(m+n)
        pA , pB = headA, headB
        # Traverse both list until they meet or reach the end
        while pA != pB: # DO dry Run
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
        # pointers will meet at intersection node after swicthing lists
        # if no intersection , both will eventually be None