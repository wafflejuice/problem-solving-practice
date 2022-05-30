import sys
import math
import heapq
from collections import deque

EMPTY = 0
FISHES = (1, 2, 3, 4, 5, 6)
SHARK = 9

n = int(sys.stdin.readline())

matrix = []

fish_idxes = []
shark_idx = None
shark_size = 2
eat_cnt = 0

for yi in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix += row
    for xi in range(len(row)):
        if row[xi] == SHARK:
            shark_idx = yi * n + xi
        elif row[xi] in FISHES:
            fish_idxes.append(yi * n + xi)

sec = 0
while True:
    q = deque()
    q.append((shark_idx, 0))
    dists = [math.inf for _ in range(n * n)]
    dists_q = []
    while len(q) > 0:
        v, dist = q.popleft()
        if dist >= dists[v]:
            continue

        dists[v] = dist
        heapq.heappush(dists_q, (dist, v // n, v % n, v))

        adjs = []
        if v % n != 0:
            adjs.append(v-1)
        if v % n != n - 1:
            adjs.append(v + 1)
        if v // n != 0:
            adjs.append(v - n)
        if v // n != n - 1:
            adjs.append(v + n)

        for adj in adjs:
            if 0 <= adj < n*n and matrix[adj] <= shark_size:
                q.append((adj, dist + 1))

    has_eaten = False
    while len(dists_q) > 0:
        dist, yi, xi, v = heapq.heappop(dists_q)
        if matrix[v] in FISHES and matrix[v] < shark_size:
            matrix[shark_idx] = EMPTY
            matrix[v] = SHARK
            shark_idx = v
            eat_cnt += 1
            if eat_cnt == shark_size:
                eat_cnt = 0
                shark_size += 1
            has_eaten = True
            sec += dist
            break

    if not has_eaten:
        break

print(sec)