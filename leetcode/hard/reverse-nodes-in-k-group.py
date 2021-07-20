# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        result = ListNode(0)
        result_tail = result
        
        while head:
            cycle = ListNode(0)
            cycle_tail = cycle
            head_save = head
            
            for i in range(k):
                if head == None: 
                    result_tail.next = head_save
                    return result.next
                    
                current = ListNode(head.val)
                tmp = cycle_tail.next
                cycle_tail.next = current
                cycle_tail.next.next = tmp
                head = head.next
                
            result_tail.next = cycle.next
            for i in range(k):
                result_tail = result_tail.next
                

        return result.next
