# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Mid
        slow = head
        fast = head
        mid = None
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # Reverse second half
        curr = mid.next
        mid.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # mid.next = prev
        # Merge two halves where first half is at head and second half is at mid
        l1 = head
        l2 = prev
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2

        


        