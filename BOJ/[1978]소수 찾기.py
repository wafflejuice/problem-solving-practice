import math
import sys

n = int(sys.stdin.readline())
nums = map(int, sys.stdin.readline().rstrip().split())

memo = [False for _ in range(1001)]
memo[2] = True
for i in range(3, 1001):
    if i % 2 == 0:
        continue

    div = 3
    while div <= math.sqrt(i):
        if i % div == 0:
            break
        div += 2
    else:
        memo[i] = True
        
cnt = 0
for num in nums:
    if memo[num]:
        cnt += 1

print(cnt)