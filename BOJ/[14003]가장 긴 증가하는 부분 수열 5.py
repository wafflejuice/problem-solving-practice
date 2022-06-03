import math
import sys
import bisect

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

memo = [math.inf for _ in range(n)] # memo[i] : length=i+1인 부분 수열의 최소 마지막 항
record = [0 for _ in range(n)]
last_idx = -1
for i in range(n):
    idx = bisect.bisect_left(memo, arr[i])
    memo[idx] = arr[i]
    record[i] = idx
    if idx > last_idx:
        last_idx = idx

trace = []
for i in range(n-1, -1, -1):
    if record[i] == last_idx:
        trace.append(arr[i])
        last_idx -= 1
trace.reverse()

print(len(trace))
print(' '.join(map(str, trace)))
