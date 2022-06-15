import bisect
import math
import sys

m, n = map(int, sys.stdin.readline().rstrip().split())

memo = [2]

def is_prime(n):
    for div in memo:
        if div > math.sqrt(n):
            break
        if n % div == 0:
            return False
    return True
    
for num in range(3, n + 1, 2):
    if is_prime(num):
        memo.append(num)

lo = bisect.bisect_left(memo, m)
for i in range(lo, len(memo)):
    print(memo[i])