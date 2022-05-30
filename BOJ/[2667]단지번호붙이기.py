import sys

n = int(sys.stdin.readline())

matrix = []
for _ in range(n):
    matrix += list(map(int, list(sys.stdin.readline().rstrip())))

graph = [[] for _ in range(n*n)]
for yi in range(n):
    for xi in range(n):
        curr_pos = yi * n + xi
        if matrix[curr_pos] == 1:
            if xi-1>=0:
                left_pos = yi * n + (xi - 1)
                if matrix[left_pos] == 1:
                    graph[curr_pos].append(left_pos)
                    graph[left_pos].append(curr_pos)
            if yi-1>=0:
                up_pos = (yi-1) * n + xi
                if matrix[up_pos] == 1:
                    graph[curr_pos].append(up_pos)
                    graph[up_pos].append(curr_pos)

num_cnt = dict()
num = 0
visit = [False for _ in range(n*n)]
for yi in range(n):
    for xi in range(n):
        curr_pos = yi*n+xi
        if matrix[curr_pos] == 0:
            continue
        if visit[curr_pos]:
            continue

        num += 1
        num_cnt[num] = 0
        stack = []
        stack.append(curr_pos)
        while len(stack) > 0:
            v = stack.pop()
            if visit[v]:
                continue
            visit[v] = True
            num_cnt[num] += 1

            for adj in graph[v]:
                stack.append(adj)

print(len(num_cnt))
for cnt in sorted(num_cnt.values()):
    print(cnt)