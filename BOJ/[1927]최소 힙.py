import sys
import heapq

n = int(sys.stdin.readline())
q = []

for ni in range(n):
    x = int(sys.stdin.readline())
    if x>0:
        heapq.heappush(q, x)
    else:
        if len(q) > 0:
            print(heapq.heappop(q))
        else:
            print(0)