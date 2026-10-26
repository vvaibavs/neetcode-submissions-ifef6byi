# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        slow = prev
        print(slow.val)

        while slow.next:
            nextnode = head.next
            nextslow = slow.next
            head.next = slow
            slow.next = nextnode
            head = nextnode
            slow = nextslow
        