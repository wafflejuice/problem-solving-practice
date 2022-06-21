import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
for i in range(n):
    q.append(i+1)
toggle = True
while len(q) > 1:
    if toggle:
        q.popleft()
    else:
        q.append(q.popleft())
    toggle = not toggle

print(q.popleft())