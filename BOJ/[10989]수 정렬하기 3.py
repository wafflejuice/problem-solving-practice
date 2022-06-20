import sys

n = int(sys.stdin.readline())
cnts = [0 for _ in range(10001)]
for _ in range(n):
    cnts[int(sys.stdin.readline())] += 1
for i, cnt in enumerate(cnts):
    if cnt > 0:
        for _ in range(cnt):
            print(i)