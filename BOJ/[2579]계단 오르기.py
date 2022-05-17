import sys

n = int(sys.stdin.readline())
scores = []
for _ in range(n):
    score = int(sys.stdin.readline())
    scores.append(score)

if n <= 2:
    print(sum(scores))
else:
    # memo[i][0] is step i-th stair and (i-1)-th stair and not (i-2)-th stair
    # memo[i][1] is step i-th stair and not (i-1)-th stair and step (i-2)-th stair
    memo = [[0, 0] for _ in range(n)]
    memo[0][0] = scores[0]
    memo[0][1] = scores[0]
    memo[1][0] = scores[0] + scores[1]
    memo[1][1] = scores[1]
    for i in range(2, n):
        memo[i][0] = memo[i-1][1] + scores[i]
        memo[i][1] = max(memo[i-2][0], memo[i-2][1]) + scores[i]
    
    print(max(memo[n-1][0], memo[n-1][1]))