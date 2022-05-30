import sys

n = int(sys.stdin.readline())
rgb_costs = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

memo = [[0, 0, 0] for _ in range(n)]
memo[0] = rgb_costs[0]
i = 1
while i < n:
    for color in range(3):
        candidates = []
        for pre_color in range(3):
            if pre_color != color:
                candidates.append(memo[i-1][pre_color] + rgb_costs[i][color])
        memo[i][color] = min(candidates)
    i += 1

print(min(memo[n-1]))