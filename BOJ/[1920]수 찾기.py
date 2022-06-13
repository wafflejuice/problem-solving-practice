import bisect
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
m = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().rstrip().split()))
for e in t:
    i = bisect.bisect_left(a, e)
    if i < n and a[i] == e:
        print(1)
    else:
        print(0)