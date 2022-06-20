import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'push':
        x = int(order[1])
        q.append(x)
    elif order[0] == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(q) > 0:
            val = q.popleft()
            print(val)
            q.appendleft(val)
        else:
            print(-1)
    elif order[0] == 'back':
        if len(q) > 0:
            val = q.pop()
            print(val)
            q.append(val)
        else:
            print(-1)