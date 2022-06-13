import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
dists = [x, w-x, y, h-y]
dists = list(map(abs, dists))
print(min(dists))