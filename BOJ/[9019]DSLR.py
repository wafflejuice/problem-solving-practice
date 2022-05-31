import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    q = deque()
    q.append((a, ''))
    visit = [False for _ in range(10000)]
    while True:
        v, ops = q.popleft()
        if visit[v]:
            continue
        visit[v] = True
        if v == b:
            print(ops)
            break
            
        q.append(((v * 2) % 10000, ops + 'D'))
        q.append(((v-1 + 10000) % 10000, ops + 'S'))
        q.append(((v*10) % 10000 + v // 1000, ops + 'L'))
        q.append((v // 10 + (v%10) * 1000, ops + 'R'))

# NOTE: submit as PyPy3