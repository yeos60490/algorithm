# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = head
        result = ListNode(0)
        result_tail = result
        size = 0
        
        while nodes:
            nodes = nodes.next
            size += 1
            
        count = -1    
        while head:
            count += 1
            if count == size-n:
                head = head.next
                continue
            result_tail.next = ListNode(head.val)
            result_tail = result_tail.next
            head = head.next
            
    
            
        return result.next
        
            
