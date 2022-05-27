import math
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    cnt = 0
    for i in range(n // 3 + 1):
        for j in range((n - 3 * i)//2 + 1):
            k = n-3*i-2*j
            cnt += math.factorial(i+j+k) // (math.factorial(i) * math.factorial(j) * math.factorial(k))

    print(cnt)