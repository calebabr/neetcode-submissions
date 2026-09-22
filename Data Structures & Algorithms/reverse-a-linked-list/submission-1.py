# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case, empty list
        if head == None:
            return None
        curr = head
        prev = None
        while curr != None:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        print(curr)
        return prev