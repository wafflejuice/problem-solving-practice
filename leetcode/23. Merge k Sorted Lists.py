from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def binaryInsort(nodesList, newNode):
    if len(nodesList)==0:
        nodesList.append(newNode)
        return

    low, high=0, len(nodesList)
    preLow, preHigh=low, high
    
    while low<high:
        mid=(low+high)//2
        
        # unstable sort
        if nodesList[mid].val==newNode.val:
            nodesList.insert(mid, newNode)
            return
        elif nodesList[mid].val<newNode.val:
            preLow=low
            low=mid+1
        else:
            preHigh=high
            high=mid
    
    if low>=high:
        for i in range(preLow, preHigh):
            if i==preLow and newNode.val < nodesList[preLow].val:
                nodesList.insert(i, newNode)
                return
            
            if i==preHigh-1 and nodesList[i].val<=newNode.val:
                nodesList.insert(i+1, newNode)
                return
            
            if nodesList[i].val<=newNode.val<nodesList[i + 1].val:
                nodesList.insert(i+1, newNode)
                return
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_vertical_list=[]
        
        # edge case
        # a list can be empty (length=0, None)
        for li in range(len(lists)):
            if lists[li] is not None:
                binaryInsort(sorted_vertical_list, lists[li])
        
        preHead = ListNode()
        curr=preHead
        while len(sorted_vertical_list)>0:
            smallest=sorted_vertical_list.pop(0)
            curr.next=smallest
            curr=curr.next
            if smallest.next is not None:
                binaryInsort(sorted_vertical_list, smallest.next)
        
        return preHead.next

def printList(l):
    while l is not None:
        print(f'{l.val}, ', end='')
        l=l.next
    print()

printList(
    Solution().mergeKLists(
        [
            ListNode(1,ListNode(4,ListNode(5))),
            ListNode(1,ListNode(3,ListNode(4))),
            ListNode(2,ListNode(6))
        ]
    )
) # [1,1,2,3,4,4,5,6]

printList(
    Solution().mergeKLists(
        [
            ListNode(-1,ListNode(1)),
            ListNode(-3,ListNode(1,ListNode(4))),
            ListNode(-2,ListNode(-1,ListNode(0,ListNode(2))))
        ]
    )
) # [-3,-2,-1,-1,0,1,1,2,4]