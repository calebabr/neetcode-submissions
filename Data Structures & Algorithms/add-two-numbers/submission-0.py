# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        totalList = ListNode()
        curr = totalList
        carry10 = 0 # how much to carry into next val

        while l1 or l2 or carry10: # check if there is a value to add from the lists OR a carried number to add
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry10 # will always be between 0-18
            carry10 = val // 10 # amount to carry into next iteration
            val = val % 10 # value to add in ones
            curr.next = ListNode(val)

            # Iterate to next
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return totalList.next

        