import bisect
import heapq
import sys

sys.setrecursionlimit(10**8)

n, k = map(int, sys.stdin.readline().rstrip().split())
cs = [0 for _ in range(k)]

parents = [i for i in range(k+1)]

def find(u):
    if u == parents[u]:
        return u
    parents[u] = find(parents[u])
    return parents[u]

def union(u, v):
    uu = find(u)
    vv = find(v)
    if uu == vv:
        return
    parents[u] = vv

q = []
for ni in range(n):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(q, (-v, m))
for ki in range(k):
    cs[ki] = int(sys.stdin.readline())
cs.sort()

ki = 0
value = 0
while ki < k:
    if len(q) == 0:
        break
    popped = heapq.heappop(q)
    v = -popped[0]
    m = popped[1]
    idx = bisect.bisect_left(cs, m)
    idx = find(idx)
    if idx < k:
        value += v
        ki += 1
        union(idx, idx+1)

print(value)