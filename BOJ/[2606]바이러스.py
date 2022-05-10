import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

stack = []
stack.append(1)
visit = []
cnt = 0
while len(stack) > 0:
    node = stack.pop()
    if node in visit:
        continue
    visit.append(node)
    cnt += 1
    for neighbor in range(1, n + 1):
        if graph[node][neighbor] > 0:
            stack.append(neighbor)

print(cnt-1)