# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #print(l1)

        sum_value = l1.val + l2.val
        carry = int(sum_value/10)
        current = int(sum_value%10)
        
        result = ListNode(current)
        l3 = result

        while l1.next or l2.next or carry:
            l1 = l1.next if l1.next != None else ListNode(0)
            l2 = l2.next if l2.next != None else ListNode(0)
        
            sum_value = l1.val + l2.val + carry
            carry = int(sum_value/10)
            current = int(sum_value%10)
            
            l3.next = ListNode(current)
            l3 = l3.next
            
        return result
