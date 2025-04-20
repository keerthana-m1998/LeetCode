# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find Mid , Slow pointer acts as head to 2nd Half of LL
        # SLow points to mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed_second = reverse(slow)
        #Compare and check
        is_palindrome = True
        first = head
        second = reversed_second
        while second:
            if first.val != second.val:
                is_palindrome = False
                break
            first = first.next
            second = second.next

        reverse(reversed_second)
        return is_palindrome

def reverse(head:ListNode)-> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev