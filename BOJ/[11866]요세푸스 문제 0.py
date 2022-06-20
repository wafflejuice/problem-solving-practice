import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

curr = -1
cnt = 0
visit = [False for _ in range(n)]
trace = []

for _ in range(n):
    d = 0
    while d < k:
        curr += 1
        curr %= n
        if not visit[curr]:
            d += 1
    visit[curr] = True
    trace.append(str(curr+1))

print('<' + ', '.join(trace) + '>')