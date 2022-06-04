import bisect
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
arr = [0 for _ in range(n)]
for ni in range(n):
    arr[ni] = int(sys.stdin.readline())

cnt = 0
hi = n
while k > 0:
    idx = bisect.bisect_right(arr, k, 0, hi) - 1
    hi = idx
    val = arr[idx]
    cnt += k // val
    k %= val

print(cnt)