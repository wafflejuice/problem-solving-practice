import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
print(' '.join(map(str, (filter(lambda elem:elem < x, a)))))