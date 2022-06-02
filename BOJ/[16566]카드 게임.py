import bisect
import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
m_nums = list(map(int, sys.stdin.readline().rstrip().split()))
m_nums.sort()
k_nums = list(map(int, sys.stdin.readline().rstrip().split()))

rep = [i for i in range(n+1)]

def find(n):
    if n == rep[n]:
        return n
    rep[n] = find(rep[n])
    return rep[n]

def union(a, b):
    u = find(a)
    v = find(b)
    if u == v:
        return
    rep[u] = v

for i in range(k):
    idx = bisect.bisect_right(m_nums, k_nums[i])
    idx = find(idx)
    print(m_nums[idx])
    union(idx, idx+1)