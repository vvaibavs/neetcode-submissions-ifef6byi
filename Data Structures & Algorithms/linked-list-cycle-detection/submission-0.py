# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashMap = {}

        while head:
            if head in hashMap:
                return True
            hashMap[head] = 1
            head = head.next
        return False