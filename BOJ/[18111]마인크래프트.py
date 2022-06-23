import math
import sys

n, m, b = map(int, sys.stdin.readline().rstrip().split())

h_cnts = [0 for _ in range(257)]
max_h, min_h = -1, -1
for _ in range(n):
    hs = list(map(int, sys.stdin.readline().rstrip().split()))
    for h in hs:
        h_cnts[h] += 1
    max_h = max(max_h, max(hs))
    min_h = min(min_h, min(hs))

min_cost = math.inf
ans_h = -1
for h in range(max_h, min_h-1, -1):
    cost = 0
    blocks = 0
    for i in range(h+1):
        if h_cnts[i] > 0:
            cost += h_cnts[i] * (h - i)
            blocks += h_cnts[i] * (h - i)
    for i in range(h+1, max_h+1):
        if h_cnts[i] > 0:
            cost += 2 * h_cnts[i] * (i - h)
            blocks -= h_cnts[i] * (i - h)

    if blocks > b:
        continue
    if cost < min_cost:
        min_cost = cost
        ans_h = h

print(str(min_cost) + ' ' + str(ans_h))