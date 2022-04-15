from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        dummy_head=ListNode(0, head)
        
        pre=dummy_head
        first=pre.next
        second=first.next
        
        while first is not None and second is not None:
            pre.next=second
            first.next=second.next
            second.next=first
            
            temp=first
            first=second
            second=temp
            
            pre=pre.next.next
            first=first.next.next
            if second.next is None:
                second=None
            else:
                second=second.next.next
        
        return dummy_head.next
    
def printList(l):
    while l is not None:
        print(f'{l.val}, ', end='')
        l=l.next
    print()

printList(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))) # [2,1,4,3]
printList(Solution().swapPairs(None)) # []
printList(Solution().swapPairs(ListNode(1))) # [1]

