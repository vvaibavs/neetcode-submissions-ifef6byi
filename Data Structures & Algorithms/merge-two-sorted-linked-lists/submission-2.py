# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        newHead = ListNode
        res = ListNode
        if l1 and l2:
            if l1.val <= l2.val:
                newHead = l1
                res = l1
                l1 = l1.next
            else:
                newHead = l2
                res = l2
                l2 = l2.next
        elif l1:
            newHead = l1
            res = l1
            l1 = l1.next
        elif l2:
            newHead = l2
            res = l2
            l2 = l2.next
        else: 
            return None

        while l1 or l2:
            if l1:
                print('hello')
                if l2:
                    if l2.val < l1.val:
                        newHead.next = l2
                        l2 = l2.next
                    elif l1.val <= l2.val:
                        newHead.next = l1
                        l1 = l1.next
                    newHead = newHead.next
                else:
                    newHead.next = l1
                    newHead = newHead.next
                    l1 = l1.next
            elif l2:
                newHead.next = l2
                newHead = newHead.next
                l2 = l2.next


        return res