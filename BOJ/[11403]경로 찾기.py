import sys

n = int(sys.stdin.readline())
graph = [list(map(str, map(int, sys.stdin.readline().split()))) for _ in range(n)]

while True:
    is_updated = False
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '0':
                for k in range(n):
                    if graph[i][k] == '1' and graph[k][j] == '1':
                        graph[i][j] = '1'
                        is_updated = True
    if not is_updated:
        break

for i in range(n):
    print(' '.join(graph[i]))