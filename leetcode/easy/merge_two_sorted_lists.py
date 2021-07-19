# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        result = ListNode(0)
        result_tail = result
        
        while l1:
            if l2 == None:
                l2 = ListNode(101)

            if l1.val < l2.val:
                result_tail.next = ListNode(l1.val)
                l1 = l1.next

            elif l1.val > l2.val:
                result_tail.next = ListNode(l2.val)
                l2 = l2.next
                
            else:
                result_tail.next = ListNode(l1.val)
                l1 = l1.next
                result_tail = result_tail.next
                result_tail.next = ListNode(l2.val)
                l2 = l2.next

            result_tail = result_tail.next
           
        
        while l2:
            if l2.val > 100:
                break
            result_tail.next = ListNode(l2.val)
            l2 = l2.next
            result_tail = result_tail.next
        
        
        return result.next
        
