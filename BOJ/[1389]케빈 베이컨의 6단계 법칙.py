import sys
import math

n, m = map(int, sys.stdin.readline().split())
graph = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

for mi in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            new_w = graph[i][k] + graph[k][j]
            if new_w < graph[i][j]:
                graph[i][j] = new_w

min_k = math.inf
min_idx = -1
for ri in range(1, n+1):
    k = 0
    for ci in range(1, n+1):
        if ri != ci:
            k += graph[ri][ci]
    if k < min_k:
        min_k = k
        min_idx = ri

print(min_idx)