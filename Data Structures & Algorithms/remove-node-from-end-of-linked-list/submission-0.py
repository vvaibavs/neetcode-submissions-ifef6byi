# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        temp = head
        dummy = ListNode(0, head)
        while temp:
            temp = temp.next
            counter+=1
        prev=dummy
        for i in range(counter-n):
            prev = prev.next
        prev.next = prev.next.next
        
        return dummy.next