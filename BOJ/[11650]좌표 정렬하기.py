import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(heap, (x, y))
while len(heap) > 0:
    x, y = heapq.heappop(heap)
    print(str(x) + ' ' + str(y))