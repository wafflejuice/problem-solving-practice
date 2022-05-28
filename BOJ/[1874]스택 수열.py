import sys
from collections import deque

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

ops = []
stack = deque()
stack.append(0)
next = 1
ai = 0
while ai < len(arr):
    if arr[ai] > next:
        stack.append(next)
        next += 1
        ops.append('+')
    elif arr[ai] == next:
        ops.append('+')
        next += 1
        ops.append('-')
        ai += 1
    else:
        top = stack.pop()
        if arr[ai] == top:
            ops.append('-')
            ai += 1
        else:
            print('NO')
            break
else:
    for op in ops:
        print(op)
