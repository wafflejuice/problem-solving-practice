import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maze = [[0 for _ in range(m)] for _ in range(n)]
active_cnt = 0
active_poses = [[0 for _ in range(m)] for _ in range(n)]
for ri in range(n):
    for ci, node in enumerate(sys.stdin.readline().rstrip()):
        if node == '1':
            maze[ri][ci] = 1
            active_poses[ri][ci] = active_cnt
            active_cnt += 1

active_nodes = []
graph = [[] for _ in range(active_cnt)]
for yi in range(n):
    for xi in range(m):
        if maze[yi][xi] == 1:
            for dy, dx in ((1, 0), (0, 1)):
                new_y = yi + dy
                new_x = xi + dx
                if new_y < n and new_x < m:
                    if maze[new_y][new_x] == 1:
                        graph_pos = active_poses[yi][xi]
                        graph_new_pos = active_poses[new_y][new_x]
                        graph[graph_pos].append(graph_new_pos)
                        graph[graph_new_pos].append(graph_pos)

start = 0
queue = deque()
queue.append((start, 1))
visit = [False for _ in range(active_cnt)]

while len(queue) > 0:
    v, move = queue.popleft()
    if visit[v]:
        continue
    if v == active_cnt-1:
        print(move)
        break
    visit[v] = True
    for adj in graph[v]:
        queue.append((adj, move+1))
