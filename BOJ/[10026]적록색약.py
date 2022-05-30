import sys

n = int(sys.stdin.readline())

matrix = []
for yi in range(n):
    matrix.append(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n*n)]
for yi in range(n):
    for xi in range(n):
        if 0<=xi-1 and matrix[yi][xi-1] == matrix[yi][xi]:
            graph[yi * n + xi].append(yi*n+(xi-1))
            graph[yi*n+(xi-1)].append(yi * n + xi)
        if 0<=yi-1 and matrix[yi-1][xi] == matrix[yi][xi]:
            graph[yi * n + xi].append((yi-1) * n + xi)
            graph[(yi-1) * n + xi].append(yi * n + xi)

def count_areas():
    visit = [False for _ in range(n * n)]
    cnt = 0
    for yi in range(n):
        for xi in range(n):
            if visit[yi * n + xi]:
                continue
            stack = []
            stack.append(yi * n + xi)
            while len(stack) > 0:
                v = stack.pop()
                if visit[v]:
                    continue
                visit[v] = True
                stack.append(v)

                for adj in graph[v]:
                    stack.append(adj)
            cnt += 1
    return cnt

ans = [0, 0]
ans[0] = count_areas()

for yi in range(n):
    for xi in range(n):
        if 0<=xi-1:
            if (matrix[yi][xi-1] == 'R' and matrix[yi][xi] == 'G') or (matrix[yi][xi-1] == 'G' and matrix[yi][xi] == 'R'):
                graph[yi * n + xi].append(yi * n + (xi-1))
                graph[yi * n + (xi-1)].append(yi * n + xi)
        if 0<=yi-1:
            if (matrix[yi-1][xi] == 'R' and matrix[yi][xi] == 'G') or (matrix[yi-1][xi] == 'G' and matrix[yi][xi] == 'R'):
                graph[yi * n + xi].append((yi-1) * n + xi)
                graph[(yi-1) * n + xi].append(yi * n + xi)

ans[1] = count_areas()

print(str(ans[0]) + ' ' + str(ans[1]))