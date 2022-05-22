import sys
from collections import deque
m, n = map(int, sys.stdin.readline().rstrip().split())

q = deque()
box = [[0 for _ in range(n)] for _ in range(m)]
unripe_cnt = 0
for ni in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for mi in range(m):
        box[mi][ni] = row[mi]
        if box[mi][ni] == 1:
            q.append((mi, ni, 0))
        elif box[mi][ni] == 0:
            unripe_cnt += 1

max_day = -1
while len(q) > 0:
    mi, ni, day = q.popleft()
    max_day = max(max_day, day)
    
    nexts = ((mi, ni + 1), (mi, ni - 1), (mi + 1, ni), (mi - 1, ni))
    
    for next in nexts:
        if not (0 <= next[0] < m and 0 <= next[1] < n):
            continue
        if box[next[0]][next[1]] == 0:
            box[next[0]][next[1]] = 1
            unripe_cnt -= 1
            q.append((next[0], next[1], day + 1))

if unripe_cnt > 0:
    print(-1)
else:
    print(max_day)