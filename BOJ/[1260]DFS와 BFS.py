import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for mi in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

stack = deque()
stack.append(v)
visit = [False for _ in range(n+1)]
path = []
while len(stack) > 0:
    node = stack.pop()
    
    if visit[node]:
        continue
    visit[node] = True
    path.append(str(node))
    
    for adj in graph[node]:
        stack.append(adj)

print(' '.join(path))

for i in range(1, n+1):
    graph[i].sort(reverse=False)
    
queue = deque()
queue.append(v)
visit = [False for _ in range(n+1)]
path = []
while len(queue) > 0:
    node = queue.popleft()

    if visit[node]:
        continue
    visit[node] = True
    path.append(str(node))
    
    for adj in graph[node]:
        queue.append(adj)

print(' '.join(path))