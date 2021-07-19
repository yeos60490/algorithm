# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        total = []
        for node in lists:
            while node:
                total.append(node.val)
                node = node.next
                
        total.sort()
        if total == []:
            return None
        
        result = ListNode(total[0])
        result_tail = result
        for i in total[1:]:
            result_tail.next = ListNode(i)
            result_tail = result_tail.next
            
        return result
                
        
