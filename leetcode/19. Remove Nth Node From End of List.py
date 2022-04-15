from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        class BidirectionalListNode:
            def __init__(self, val=0, next=None, pre=None):
                self.val = val
                self.next = next
                self.pre = pre
                
        bi_pre_head = BidirectionalListNode()
        bi_curr = bi_pre_head
        curr=head
        while curr is not None:
            new_bi_curr=BidirectionalListNode(curr.val, None, bi_curr)
            bi_curr.next = new_bi_curr
            
            bi_curr = bi_curr.next
            curr=curr.next
            
        for i in range(n-1):
            bi_curr = bi_curr.pre
            
        if bi_curr.pre is not None:
            bi_curr.pre.next=bi_curr.next
        if bi_curr.next is not None:
            bi_curr.next.pre=bi_curr.pre
        
        return bi_pre_head.next
    
def printList(l):
    while l is not None:
        print(f'{l.val}, ', end='')
        l = l.next
    print()

l=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
printList(Solution().removeNthFromEnd(l, 2)) # [1,2,3,5]

l=ListNode(1)
printList(Solution().removeNthFromEnd(l, 1)) # []

l=ListNode(1,ListNode(2))
printList(Solution().removeNthFromEnd(l, 1)) # [1]