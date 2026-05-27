# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        place = 1
        curr = l1
        while curr is not None:
            num1 += curr.val * place
            place *= 10
            curr = curr.next

        num2 = 0
        place = 1
        curr = l2
        while curr is not None:
            num2 += curr.val * place
            place *= 10
            curr = curr.next

        totalSum = num1 + num2

        # Convert to digit list
        sumList = []
        if totalSum == 0:          # 0 + 0 + 0
            sumList = [0]
        while totalSum != 0:
            sumList.append(totalSum % 10)
            totalSum //= 10

        # Build the linked list
        dummy = ListNode(0)
        curr = dummy
        for digit in sumList:
            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next