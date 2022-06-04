import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
q = deque()
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [False for _ in range(n+1)]
cnt = 0
for i in range(1, n+1):
    if visit[i]:
        continue
    q.append(i)
    cnt += 1

    while len(q) > 0:
        v = q.popleft()
        if visit[v]:
            continue
        visit[v] = True
        for adj in graph[v]:
            q.append(adj)
            
print(cnt)