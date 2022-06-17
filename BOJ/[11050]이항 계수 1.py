import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
val = 1
for i in range(k):
    val *= (n-i)
for i in range(k):
    val //= (k-i)
print(val)