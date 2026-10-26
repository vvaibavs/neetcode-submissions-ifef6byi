# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if not l1:
            return l2
        elif not l2:
            return l1
        headnode = ListNode
        res = ListNode
        if l1.val > l2.val:
            headnode = l2
            res = l2
            l2 = l2.next
        else:
            headnode = l1
            res = l1
            l1 = l1.next
        
        while l1 or l2:
            if l1:
                if l2:
                    if l1.val > l2.val:
                        headnode.next = l2
                        l2 = l2.next
                    elif l2.val >= l1.val:
                        headnode.next = l1
                        l1 = l1.next
                    headnode = headnode.next
                else:
                    headnode.next = l1
                    l1 = l1.next
                    headnode = headnode.next
            else:
                headnode.next = l2
                l2 = l2.next
                headnode = headnode.next
        return res

