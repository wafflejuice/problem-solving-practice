import sys
from collections import deque

n = int(sys.stdin.readline())
lines = []
for _ in range(n):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().rstrip().split()))
    if x1 < x2 or (x1 == x2 and y1 <= y2):
        lines.append((x1, y1, x2, y2))
    else:
        lines.append((x2, y2, x1, y1))

groups = [[] for _ in range(n)]
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        sx1, sy1, ex1, ey1 = lines[i]
        sx2, sy2, ex2, ey2 = lines[j]
        
        if ex1 < sx2 or ex2 < sx1:
            continue
            
        xs = sorted([sx1, ex1, sx2, ex2])
        cross_sx, cross_ex = xs[1], xs[2]

        if ex1-sx1 == 0:
            cross_sy1 = sy1
            cross_ey1 = ey1
        else:
            cross_sy1 = (ey1 - sy1) / (ex1 - sx1) * (cross_sx - sx1) + sy1
            cross_ey1 = (ey1 - sy1) / (ex1 - sx1) * (cross_ex - sx1) + sy1
        
        if ex2-sx2 == 0:
            cross_sy2 = sy2
            cross_ey2 = ey2
        else:
            cross_sy2 = (ey2 - sy2) / (ex2 - sx2) * (cross_sx - sx2) + sy2
            cross_ey2 = (ey2 - sy2) / (ex2 - sx2) * (cross_ex - sx2) + sy2
        
        if (cross_sy1 - cross_sy2)*(cross_ey1 - cross_ey2) <= 0:
            groups[i].append(j)
            groups[j].append(i)

visit = [False for _ in range(n)]
curr = 0
cnt = 0
max_group_size = -1
while curr < n:
    stack = deque()
    stack.append(curr)
    group_size = 0
    while len(stack) > 0:
        v = stack.pop()
        if visit[v]:
            continue
        visit[v] = True
        group_size += 1
        
        for adj in groups[v]:
            stack.append(adj)
    
    if group_size > 0:
        max_group_size = max(max_group_size, group_size)
        cnt += 1
        
    curr += 1

print(cnt)
print(max_group_size)