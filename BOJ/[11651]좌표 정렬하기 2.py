import heapq
import sys

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(q, (y, x))
for _ in range(n):
    y, x = heapq.heappop(q)
    print(str(x) + ' ' + str(y))