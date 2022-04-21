from typing import *
import math
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def inorder(self, root, visit):
        q=deque()
        q.append(root)
        while len(q)>0:
            n=q.popleft()
            if n.left:
                self.inorder(n.left, visit)
            visit.append(n.val)
            if n.right:
                self.inorder(n.right, visit)

    def __init__(self, root: Optional[TreeNode]):
        self.val = -math.inf
        visit=deque()
        self.inorder(root, visit)
        self.visit = visit

    def next(self) -> int:
        return self.visit.popleft()

    def hasNext(self) -> bool:
        return len(self.visit) > 0

def print_tree(root):
    if root is None:
        print('None, ', end='')
    else:
        print(f'{root.val}, ', end='')
        print_tree(root.left)
        print_tree(root.right)

root = TreeNode(7,TreeNode(3),TreeNode(15,TreeNode(9),TreeNode(20)))
operations = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
for op in operations:
    if op == "BSTIterator":
        itr = BSTIterator(root)
        print('None', end=' ')
    elif op == "hasNext":
        has_next = itr.hasNext()
        print(has_next, end=' ')
    elif op == "next":
        next_val = itr.next()
        print(next_val, end=' ')
print()