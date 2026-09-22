# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case, empty list. not necessary
        if head == None:
            return None
        curr = head
        prev = None
        while curr != None:
            n = curr.next # save next value because curr will eventially be come this
            curr.next = prev # point curr to previous value
            prev = curr # previous value now becomes curr
            curr = n # curr becomes saved value
        print(curr)
        return prev