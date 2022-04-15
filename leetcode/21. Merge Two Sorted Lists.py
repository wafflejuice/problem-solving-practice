from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head=ListNode()
        curr=pre_head
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next

        while list1 is not None:
            curr.next = list1
            list1=list1.next
            curr=curr.next
            
        while list2 is not None:
            curr.next = list2
            list2=list2.next
            curr=curr.next
        
        return pre_head.next

def printList(l):
    while l is not None:
        print(f'{l.val}, ', end='')
        l=l.next
    print()

printList(Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))) # [1,1,2,3,4,4]
printList(Solution().mergeTwoLists(None, None))
printList(Solution().mergeTwoLists(None, ListNode(0)))
