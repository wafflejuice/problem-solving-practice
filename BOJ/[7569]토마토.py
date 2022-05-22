import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().rstrip().split())

q = deque()
box = [[[0 for _ in range(h)] for _ in range(n)] for _ in range(m)]
unripe_cnt = 0
for hi in range(h):
    for ni in range(n):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        for mi in range(m):
            box[mi][ni][hi] = row[mi]
            if box[mi][ni][hi] == 1:
                q.append((mi, ni, hi, 0))
            elif box[mi][ni][hi] == 0:
                unripe_cnt += 1
                
max_day = -1
while len(q) > 0:
    mi, ni, hi, day = q.popleft()
    max_day = max(max_day, day)
    
    nexts = ((mi, ni, hi+1), (mi, ni, hi-1), (mi, ni+1, hi), (mi, ni-1, hi), (mi+1, ni, hi), (mi-1, ni, hi))
    
    for next in nexts:
        if not (0 <= next[0] < m and 0 <= next[1] < n and 0 <= next[2] < h):
            continue
        if box[next[0]][next[1]][next[2]] == 0:
            box[next[0]][next[1]][next[2]] = 1
            unripe_cnt -= 1
            q.append((next[0], next[1], next[2], day + 1))
            
if unripe_cnt > 0:
    print(-1)
else:
    print(max_day)