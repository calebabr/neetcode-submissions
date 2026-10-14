# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Get to mid
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # Sever and then reverse second half
        curr = mid.next
        prev = None
        mid.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # Now prev is start of second half

        # walk both halves checking equality
        curr = head
        second = prev
        while second and curr:
            if second.val != curr.val:
                return False
            second = second.next
            curr = curr.next
        return True