import sys
import math

n, m = map(int, sys.stdin.readline().rstrip().split())

ladders = dict()
snakes = dict()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    ladders[x] = y
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    snakes[u] = v

memo = [math.inf for _ in range(101)]
memo[1] = 0

stack = []
stack.append(1)

while len(stack) > 0:
    v = stack.pop()

    candidates = []
    if v in ladders:
        if memo[v] < memo[ladders[v]]:
            memo[ladders[v]] = memo[v]
            stack.append(ladders[v])
    elif v in snakes:
        if memo[v] < memo[snakes[v]]:
            memo[snakes[v]] = memo[v]
            stack.append(snakes[v])
    else:
        for d in range(1, 7):
            if v + d > 100:
                break
            if memo[v] + 1 < memo[v + d]:
                memo[v + d] = memo[v] + 1
                stack.append(v + d)

print(memo[100])