import sys

h, m = map(int, sys.stdin.readline().rstrip().split())
time = (h * 60 + m - 45) % (24 * 60)
print(str(time // 60) + ' ' + str(time % 60))