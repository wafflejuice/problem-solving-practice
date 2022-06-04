import itertools
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[True for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = False
    graph[b][a] = False

combs = itertools.combinations((i for i in range(1, n+1)), 3)
cnt = 0
for comb in combs:
    if not graph[comb[0]][comb[1]] or not graph[comb[0]][comb[2]] or not graph[comb[1]][comb[2]]:
        continue
    cnt += 1

print(cnt)