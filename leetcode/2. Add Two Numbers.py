# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode()
        pre = head
        cast = 0
        while l1 is not None and l2 is not None:
            sum_ = l1.val + l2.val + cast
            cast = sum_ // 10
            sum_ %= 10
            print(sum_, cast)
            
            cur = ListNode(sum_)
            pre.next = cur
            pre = cur
            
            l1 = l1.next
            l2 = l2.next
            
        if l1 is None:
            while l2 is not None:
                sum_ = l2.val + cast
                cast = sum_ // 10
                sum_ %= 10
                print(sum_, cast)
            
                cur = ListNode(sum_)
                pre.next = cur
                pre = cur
                    
                l2 = l2.next
        else:
            while l1 is not None:
                sum_ = l1.val + cast
                cast = sum_ // 10
                sum_ %= 10
                print(sum_, cast)
            
                cur = ListNode(sum_)
                pre.next = cur
                pre = cur
                    
                l1 = l1.next
        
        if cast == 1:
            cur = ListNode(1)
            pre.next = cur
            pre = cur
        
        return head.next