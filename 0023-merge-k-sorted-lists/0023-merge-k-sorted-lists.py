# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(l1,l2):
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val<l2.val:
                current.next=l1
                l1 = l1.next
            else:
                current.next = l2 
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return mergeTwoLists(left,right)
    