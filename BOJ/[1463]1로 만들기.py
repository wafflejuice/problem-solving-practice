n = int(input())

memo = [n for _ in range(n+1)]
memo[n] = 0
def dp(n):
    for i in range(n, 0, -1):
        if i % 3 == 0:
            if memo[i // 3] > memo[i] + 1:
                memo[i // 3] = memo[i] + 1
        if i % 2 == 0:
            if memo[i // 2] > memo[i] + 1:
                memo[i // 2] = memo[i] + 1
    
        if memo[i - 1] > memo[i] + 1:
            memo[i - 1] = memo[i] + 1
    
    return memo[1]

print(dp(n))