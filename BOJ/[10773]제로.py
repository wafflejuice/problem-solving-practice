import sys
from collections import deque

k = int(sys.stdin.readline())
q = deque()
for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        q.pop()
    else:
        q.append(num)
print(sum(q))