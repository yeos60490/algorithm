
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        search = head.next
     
        result = ListNode(0)
        result_tail = result

        count = 0
        while search:
            if count%2 == 0:
                result_tail.next = ListNode(search.val)
                result_tail.next.next = ListNode(head.val)
                result_tail = result_tail.next.next
                        
            search = search.next 
            head = head.next
            count += 1
        
        
        head = head.next if count%2==1 else head
        
        if head:
            result_tail.next = ListNode(head.val)
            
        return result.next
